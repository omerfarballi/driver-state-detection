# driver-state-detection

The Torch library was used in the development of the artificial intelligence model architecture, which was developed for the driver control system planned to be used in smart vehicles. As the data set, approximately 1000 data developed by the Arge-Elektrik team and the data shared within the scope of the State Farm Distracted Driver Detection competition over the Kaggle platform were used. The distribution of these data is shown in Figure 1.

![image](https://user-images.githubusercontent.com/71135790/190692213-a0f04b2e-b8a6-44ea-b923-0493db498140.png)

Figure 1

10-degree rotations were applied to the random data in the data set in order to prevent overfitting of the model and to reduce the errors that may occur during use. transforms for this operation. Data augmentation was performed using the RandomRotation function. In the data set given to the model during training, the bacth size value is set to 32. The sigmoid function was preferred as the activation function of the model used in education, the learning rate value was 0.01, and the Cross entropy Loss function was preferred as the Loss function. UNet with ResNet50 architecture was used as the model architecture. The success rate in the tests is 99.45%.


In figure 2, a qt-based interface was developed and the artificial intelligence model was integrated. When the Run button is clicked on this interface, the estimated status is printed in the textfiled section. On the left side of the figure, the output obtained when the codes are run is observed.


![image](https://user-images.githubusercontent.com/71135790/190696376-cd6cdfc9-ff86-4186-9458-685c9b656c5c.png)

Figure 2

Video of the system resulting from the integration of RPi and the artificial intelligence model:
The Video link : https://drive.google.com/file/d/1k3tTeFBOT9MmegBEP8uuduax5WEsb6fN/view
