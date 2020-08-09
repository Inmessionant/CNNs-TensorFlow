from torchstat import stat
import torchvision.models as models

model = models.alexnet()
stat(model, (3, 224, 224))