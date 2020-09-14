from ..utils import downloads
from .. import image
from . import submodules

with submodules.import_from('neural-style-pt'):
    from model import *
    from utils import *
    from generate import *

    
def test():
    # setup stylenet
    params = StylenetArgs()
    params.gpu = '0'
    params.backend = 'cudnn'
    params.model_file = downloads.download_neural_style(
        'https://web.eecs.umich.edu/~justincj/models/vgg19-d01eb7cb.pth', 
        'neural_style/vgg19-d01eb7cb.pth')
    
    dtype, multidevice, backward_device = setup_gpu(params)
    stylenet = StyleNet(params, dtype, multidevice, backward_device, verbose=False)

    config = {
        'content_image': '../../assets/dog.jpg',
        'style_image': '../../assets/kitty.jpg'
    }

    img = style_transfer(stylenet, config)
    image.display(img)
    
