from PIL import Image
import os
from typing import Tuple, Optional
import logging

class ImageCompressionError(Exception):
    """自定義圖片壓縮相關的錯誤"""
    pass

def compress_image(
    input_path: str,
    output_path: str,
    max_size_mb: float = 1.0,
    min_quality: int = 20,
    min_dimension: int = 500,
    initial_quality: int = 95
) -> Tuple[float, dict]:
    """
    壓縮圖片至指定的最大檔案大小，同時保持可接受的圖片品質
    
    Parameters:
    -----------
    input_path : str
        輸入圖片的路徑
    output_path : str
        輸出圖片的路徑
    max_size_mb : float, optional
        最大檔案大小(MB)，預設為1MB
    min_quality : int, optional
        最低可接受的圖片品質(1-100)，預設為20
    min_dimension : int, optional
        最小可接受的圖片尺寸(像素)，預設為500
    initial_quality : int, optional
        初始壓縮品質，預設為95
        
    Returns:
    --------
    Tuple[float, dict]
        回傳最終檔案大小(MB)和處理過程的資訊
        
    Raises:
    -------
    ImageCompressionError
        當圖片無法壓縮到指定大小時拋出錯誤
    """
    # 設定日誌
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)
    
    # 檢查輸入檔案是否存在
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"找不到輸入檔案: {input_path}")
    
    # 檢查參數有效性
    if max_size_mb <= 0:
        raise ValueError("最大檔案大小必須大於0")
    if not (1 <= min_quality <= 100):
        raise ValueError("最低品質必須在1到100之間")
    if min_dimension < 1:
        raise ValueError("最小尺寸必須大於0")
        
    try:
        # 開啟圖片
        img = Image.open(input_path)
        
        # 儲存原始資訊
        original_size = os.path.getsize(input_path) / (1024 * 1024)
        original_dimensions = img.size
        
        # 轉換為RGB模式（如果是RGBA）
        if img.mode == 'RGBA':
            img = img.convert('RGB')
            
        # 處理資訊追蹤
        info = {
            'original_size_mb': original_size,
            'original_dimensions': original_dimensions,
            'final_quality': initial_quality,
            'final_dimensions': original_dimensions,
            'compression_steps': []
        }
        
        quality = initial_quality
        current_img = img
        
        # 先嘗試只降低品質
        while quality >= min_quality:
            current_img.save(output_path, 'JPEG', quality=quality)
            current_size = os.path.getsize(output_path) / (1024 * 1024)
            
            info['compression_steps'].append({
                'action': 'quality_reduction',
                'quality': quality,
                'size_mb': current_size
            })
            
            if current_size <= max_size_mb:
                info['final_quality'] = quality
                return current_size, info
                
            quality -= 5
            
        # 如果降低品質還不夠，開始縮減尺寸
        scale_factor = 0.9
        while True:
            width, height = current_img.size
            if width < min_dimension or height < min_dimension:
                raise ImageCompressionError(
                    f"無法達到目標大小 {max_size_mb}MB。"
                    f"最終大小: {current_size}MB"
                )
                
            new_width = int(width * scale_factor)
            new_height = int(height * scale_factor)
            current_img = img.resize(
                (new_width, new_height),
                Image.Resampling.LANCZOS
            )
            
            current_img.save(output_path, 'JPEG', quality=quality)
            current_size = os.path.getsize(output_path) / (1024 * 1024)
            
            info['compression_steps'].append({
                'action': 'resize',
                'dimensions': (new_width, new_height),
                'size_mb': current_size
            })
            
            if current_size <= max_size_mb:
                info['final_dimensions'] = (new_width, new_height)
                return current_size, info
                
    except Exception as e:
        logger.error(f"壓縮過程發生錯誤: {str(e)}")
        raise
        
    return current_size, info
