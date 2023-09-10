from bing_images import bing

bing.download_images("water pipe leak",
                      900,
                      output_dir="waterleak",
                      pool_size=10000,
                      filters='+filterui:aspect-square',
                      force_replace=True)