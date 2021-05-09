{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled0.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyN0A+i5Tv1gS9XQ9HPuC/ME",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/sunmin-lee99/Euron-AI-2021/blob/Week_4/softmax.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "VbS3lO2SC5yh"
      },
      "source": [
        "from builtins import range\n",
        "import numpy as np\n",
        "from random import shuffle\n",
        "from past.builtins import xrange\n",
        "\n",
        "\n",
        "def softmax_loss_naive(W, X, y, reg):\n",
        "    \"\"\"\n",
        "    Softmax loss function, naive implementation (with loops)\n",
        "\n",
        "    Inputs have dimension D, there are C classes, and we operate on minibatches\n",
        "    of N examples.\n",
        "\n",
        "    Inputs:\n",
        "    - W: A numpy array of shape (D, C) containing weights.\n",
        "    - X: A numpy array of shape (N, D) containing a minibatch of data.\n",
        "    - y: A numpy array of shape (N,) containing training labels; y[i] = c means\n",
        "      that X[i] has label c, where 0 <= c < C.\n",
        "    - reg: (float) regularization strength\n",
        "\n",
        "    Returns a tuple of:\n",
        "    - loss as single float\n",
        "    - gradient with respect to weights W; an array of same shape as W\n",
        "    \"\"\"\n",
        "    # Initialize the loss and gradient to zero.\n",
        "    loss = 0.0\n",
        "    dW = np.zeros_like(W)\n",
        "\n",
        "    #############################################################################\n",
        "    # TODO: Compute the softmax loss and its gradient using explicit loops.     #\n",
        "    # Store the loss in loss and the gradient in dW. If you are not careful     #\n",
        "    # here, it is easy to run into numeric instability. Don't forget the        #\n",
        "    # regularization!                                                           #\n",
        "    #############################################################################\n",
        "    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****\n",
        "\n",
        "    pass\n",
        "\n",
        "    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****\n",
        "\n",
        "    return loss, dW\n",
        "\n",
        "\n",
        "def softmax_loss_vectorized(W, X, y, reg):\n",
        "    \"\"\"\n",
        "    Softmax loss function, vectorized version.\n",
        "\n",
        "    Inputs and outputs are the same as softmax_loss_naive.\n",
        "    \"\"\"\n",
        "    # Initialize the loss and gradient to zero.\n",
        "    loss = 0.0\n",
        "    dW = np.zeros_like(W)\n",
        "\n",
        "    #############################################################################\n",
        "    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #\n",
        "    # Store the loss in loss and the gradient in dW. If you are not careful     #\n",
        "    # here, it is easy to run into numeric instability. Don't forget the        #\n",
        "    # regularization!                                                           #\n",
        "    #############################################################################\n",
        "    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****\n",
        "\n",
        "    pass\n",
        "\n",
        "    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****\n",
        "\n",
        "    return loss, dW"
      ],
      "execution_count": 3,
      "outputs": []
    }
  ]
}