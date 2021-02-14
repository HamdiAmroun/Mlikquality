import matplotlib.pyplot as plt
from datetime import datetime

def plot_loss(history):
    plt.plot(history.history['loss'], label='loss')
    plt.plot(history.history['val_loss'], label='val_loss')
#     plt.ylim([0, 10])
    plt.xlabel('Epoch')
    plt.ylabel('Error')
    plt.legend()
    plt.grid(True)

def get_datetime():
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y.%H.%M.%S")
    return dt_string