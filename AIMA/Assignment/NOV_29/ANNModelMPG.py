import math
import warnings

import numpy as np
import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split

warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', 1000)  # or 1000
pd.set_option('display.max_rows', 1000)  # or 1000
pd.set_option('display.max_colwidth', 199)  # or 199
pd.set_option('display.expand_frame_repr', False)


class Connection:
    def __init__(self, connectedNeuron):
        self.connectedNeuron = connectedNeuron
        self.weight = np.random.normal()
        self.dWeight = 0.0


class Neuron:
    eta = 0.001
    alpha = 0.01

    def __init__(self, layer):
        self.dendrons = []
        self.error = 0.0
        self.gradient = 0.0
        self.output = 0.0
        if layer is None:
            pass
        else:
            for neuron in layer:
                con = Connection(neuron)
                self.dendrons.append(con)

    def addError(self, err):
        self.error = self.error + err

    def sigmoid(self, x):
        if x > 0:
            return 1 / (1 + math.exp(-x * 1.0))
        return 1 / (1 + math.exp(x * 1.0))

    def dSigmoid(self, x):
        return x * (1.0 - x)

    def setError(self, err):
        self.error = err

    def setOutput(self, output):
        self.output = output

    def getOutput(self):
        return self.output

    def feedForword(self):
        sumOutput = 0
        if len(self.dendrons) == 0:
            return
        for dendron in self.dendrons:
            sumOutput = sumOutput + dendron.connectedNeuron.getOutput() * dendron.weight
        self.output = self.sigmoid(sumOutput)

    def backPropagate(self):
        self.gradient = self.error * self.dSigmoid(self.output);
        for dendron in self.dendrons:
            dendron.dWeight = Neuron.eta * (
                    dendron.connectedNeuron.output * self.gradient) + self.alpha * dendron.dWeight;
            dendron.weight = dendron.weight + dendron.dWeight;
            dendron.connectedNeuron.addError(dendron.weight * self.gradient);
        self.error = 0;


class Network:

    def __init__(self, topology):
        self.layers = []
        numNeuron: object
        for numNeuron in topology:
            layer = []
            for i in range(numNeuron):
                if (len(self.layers) == 0):
                    layer.append(Neuron(None))
                else:
                    layer.append(Neuron(self.layers[-1]))
            layer.append(Neuron(None))
            layer[-1].setOutput(1)
            self.layers.append(layer)

    def setInput(self, inputs):
        for i in range(len(inputs)):
            self.layers[0][i].setOutput(inputs[i])

    def feedForword(self):
        for layer in self.layers[1:]:
            for neuron in layer:
                neuron.feedForword();

    def backPropagate(self, target):
        if np.dtype(target) not in [np.float32, np.float64, np.integer]:
            for i in range(len(target)):
                self.layers[-1][i].setError(target[i] - self.layers[-1][i].getOutput())
        else:
            self.layers[-1][0].setError(target - self.layers[-1][0].getOutput())
        for layer in self.layers[::-1]:
            for neuron in layer:
                neuron.backPropagate()

    def getError(self, target):
        err = 0
        if np.dtype(target) not in [np.float32, np.float64, np.integer]:
            for i in range(len(target)):
                e = (target[i] - self.layers[-1][i].getOutput())
                # err = err + e ** 2
                err = err + e
            err = err / len(target)
        else:
            e = (target - self.layers[-1][0].getOutput())
            # err = err + e ** 2
            err = err + e

        # err = math.sqrt(err)
        return err

    def getResults(self):
        output = []
        for neuron in self.layers[-1]:
            print(neuron.output)
            output.append(neuron.getOutput())
        output.pop()
        return output.pop()

    def getTestResults(self):
        output = []
        for neuron in self.layers[-1]:
            o = neuron.getOutput()
            output.append(o)
        output.pop()
        return output


class Cars:

    def __init__(self, file, outputColumns, inputColumns=None, ignoreColumns=None):

        self.dataSet = pd.read_csv(file)
        self.fill_missing_data_columns()

        if outputColumns is None:
            raise ValueError("Missing Output Column Data !!!")
        self.outputColumns = []
        if type(outputColumns) == 'object':
            for column in outputColumns:
                self.outputColumns.append(column)
        else:
            self.outputColumns = outputColumns

        self.output = np.array(list(self.dataSet[self.outputColumns].values))

        self.inputColumns = []
        if inputColumns is None:
            for column in self.dataSet.columns:
                if column not in outputColumns and not (column.startswith(ignoreColumns) or column in ignoreColumns):
                    self.inputColumns.append(column)
        else:
            self.inputColumns = inputColumns

        self.input = np.array(list(self.dataSet[self.inputColumns].values))
        self.inputTrain, self.inputTest, self.outputTrain, self.outputTest = train_test_split(self.input, self.output,
                                                                                              test_size=0.1)

    def fill_missing_data_columns(self):
        dataSetColumns = self.dataSet.columns
        for column in dataSetColumns:
            if self.dataSet[column].dtype != "object":
                self.dataSet[column] = self.dataSet[column].fillna(self.dataSet[column].mean())
            else:
                self.dataSet[column] = self.dataSet[column].fillna('')
        return self.dataSet

    def printDataSet(self):
        print(f"\nDataSet \n\n", self.dataSet)

    def printInputColumns(self):
        print(f"Input Columns : ", self.inputColumns)

    def printOutputColumns(self):
        print(f"Output Columns : ", self.outputColumns)

    def printInputDataset(self):
        print(f"\nInput Data Set \n\n", self.input)

    def printOutputDataset(self):
        print(f"\nOutput Data Set \n\n", self.output)


if __name__ == '__main__':
    # main()

    # Input Sections
    cars = Cars("mtcars.csv", outputColumns="mpg", ignoreColumns="Unnamed:")
    cars.printDataSet()
    cars.printInputColumns()
    cars.printOutputColumns()
    cars.printInputDataset()
    cars.printOutputDataset()

    # Create the Neural Network Topology
    topology = [len(cars.inputColumns), (len(cars.inputColumns) * 2), len(cars.inputColumns), 1]
    net = Network(topology)
    Neuron.eta = 0.99
    Neuron.alpha = 0.099
    while True:

        err = 0
        inputs = cars.inputTrain
        outputs = cars.outputTrain
        for i in range(len(inputs)):
            print("Input : ", inputs[i])
            print("Output : ", outputs[i])
            net.setInput(inputs[i])
            net.feedForword()
            net.backPropagate(outputs[i])
            print("Neural Network Output : ", net.getResults())
            err = err + net.getError(outputs[i])
        print("error: ", err)
        if err < 0.01:
            break

    index = 0
    for layer in net.layers:
        print("\nLayers : ", index)
        weights = 0
        for dendron in layer.dendrons:
            print("Weights - ", weights, dendron.weight)
            weights += 1
        index += 1
    net.setInput(cars.inputTest)
    net.feedForword()
    testOutput = net.getTestResults()
    print("Test MAE : ", sklearn.metrics.mean_absolute_error(cars.outputTest, testOutput))
    print("Test RMSE : ", np.sqrt(sklearn.metrics.mean_squared_error(cars.outputTest, testOutput)))
