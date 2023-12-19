from PIL import Image
from osgeo import gdal
import cv2
import numpy as np

Image.MAX_IMAGE_PIXELS = 933120000


# # Load the raster image (replace 'your_image.tif' with the path to your image)
# image = cv2.imread('out/sarnonoharjo_01.png', cv2.IMREAD_COLOR)
# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# # Reverse the values (0 to 1 and 1 to 0)
# reversed_image = np.where(image == 0, 1, 0).astype(np.uint8)

# # Save the reversed image
# cv2.imwrite('out/sarnonoharjo_01.png', reversed_image)

# convert format
img = Image.open('dataset/coba_export/ortho_Kav4_15cm_building_result.png')
img.save('dataset/coba_export/ortho_Kav4_15cm_building_result.tif')

# buka raster
ds = gdal.Open('dataset/coba_export/ortho_Kav4_15cm_building_result.tif', gdal.GA_Update)
ref = gdal.Open('dataset/coba_export/ortho_Kav4_15cm.tif', gdal.GA_Update)

# get geotransform
gt1 = ds.GetGeoTransform()
gt2 = ref.GetGeoTransform()

# assign geotransform
ds.SetGeoTransform(gt2)
print(ds)

ds.FlushCache()
ds = None
# gdal_edit.py -a_srs EPSG:32749 ugm_35.tif

# # tif2png
# # Open the TIFF image
# tiff_image = Image.open('data/ugm/3_FT_SEPT_2022_5cm.tif')

# # Save it as a PNG image
# tiff_image.save('data/ugm/FT_2022_5cm.png', format='PNG')

# # Close the TIFF image
# tiff_image.close()