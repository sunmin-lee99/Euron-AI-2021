{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "softmax.ipynb",
      "provenance": [],
      "include_colab_link": true
    },
    "language_info": {
      "name": "python"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
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
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 964
        },
        "id": "G97rTlWIx78l",
        "outputId": "cd7f10dc-8654-4abc-ac0a-872fd13b7ba9"
      },
      "source": [
        "# This mounts your Google Drive to the Colab VM.\n",
        "from google.colab import drive\n",
        "drive.mount('/content/drive', force_remount=True)\n",
        "\n",
        "# Enter the foldername in your Drive where you have saved the unzipped\n",
        "# assignment folder, e.g. 'cs231n/assignments/assignment1/'\n",
        "FOLDERNAME = '/content/drive/MyDrive/drive/My drive/cs231n/assignments/datasets'\n",
        "assert FOLDERNAME is not None, \"[!] Enter the foldername.\"\n",
        "\n",
        "# Now that we've mounted your Drive, this ensures that\n",
        "# the Python interpreter of the Colab VM can load\n",
        "# python files from within it.\n",
        "import sys\n",
        "sys.path.append('/content/drive/My Drive/{}'.format(FOLDERNAME))\n",
        "\n",
        "# This downloads the CIFAR-10 dataset to your Drive\n",
        "# if it doesn't already exist.\n",
        "%cd drive/My\\ Drive/$FOLDERNAME/cs231n/datasets/\n",
        "!bash get_datasets.sh\n",
        "%cd /content/drive/My\\ Drive/$FOLDERNAME"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "ERROR:root:Internal Python error in the inspect module.\n",
            "Below is the traceback from this internal error.\n",
            "\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "Mounted at /content/drive\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/interactiveshell.py\", line 2882, in run_code\n",
            "    exec(code_obj, self.user_global_ns, self.user_ns)\n",
            "  File \"<ipython-input-16-8fdd28cd0749>\", line 18, in <module>\n",
            "    get_ipython().magic('cd drive/My\\\\ Drive/$FOLDERNAME/cs231n/datasets/')\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/interactiveshell.py\", line 2160, in magic\n",
            "    return self.run_line_magic(magic_name, magic_arg_s)\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/interactiveshell.py\", line 2081, in run_line_magic\n",
            "    result = fn(*args,**kwargs)\n",
            "  File \"<decorator-gen-84>\", line 2, in cd\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/magic.py\", line 188, in <lambda>\n",
            "    call = lambda f, *a, **k: f(*a, **k)\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/magics/osm.py\", line 288, in cd\n",
            "    oldcwd = py3compat.getcwd()\n",
            "OSError: [Errno 107] Transport endpoint is not connected\n",
            "\n",
            "During handling of the above exception, another exception occurred:\n",
            "\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/interactiveshell.py\", line 1823, in showtraceback\n",
            "    stb = value._render_traceback_()\n",
            "AttributeError: 'OSError' object has no attribute '_render_traceback_'\n",
            "\n",
            "During handling of the above exception, another exception occurred:\n",
            "\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/ultratb.py\", line 1132, in get_records\n",
            "    return _fixed_getinnerframes(etb, number_of_lines_of_context, tb_offset)\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/ultratb.py\", line 313, in wrapped\n",
            "    return f(*args, **kwargs)\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/ultratb.py\", line 358, in _fixed_getinnerframes\n",
            "    records = fix_frame_records_filenames(inspect.getinnerframes(etb, context))\n",
            "  File \"/usr/lib/python3.7/inspect.py\", line 1502, in getinnerframes\n",
            "    frameinfo = (tb.tb_frame,) + getframeinfo(tb, context)\n",
            "  File \"/usr/lib/python3.7/inspect.py\", line 1460, in getframeinfo\n",
            "    filename = getsourcefile(frame) or getfile(frame)\n",
            "  File \"/usr/lib/python3.7/inspect.py\", line 696, in getsourcefile\n",
            "    if getattr(getmodule(object, filename), '__loader__', None) is not None:\n",
            "  File \"/usr/lib/python3.7/inspect.py\", line 725, in getmodule\n",
            "    file = getabsfile(object, _filename)\n",
            "  File \"/usr/lib/python3.7/inspect.py\", line 709, in getabsfile\n",
            "    return os.path.normcase(os.path.abspath(_filename))\n",
            "  File \"/usr/lib/python3.7/posixpath.py\", line 383, in abspath\n",
            "    cwd = os.getcwd()\n",
            "OSError: [Errno 107] Transport endpoint is not connected\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "error",
          "ename": "OSError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "v_Fg3Ne40vyz",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "3a309b1c-b11e-4eb0-a3ad-d7f3455443ba"
      },
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount(\"/content/drive\", force_remount=True).\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "tags": [
          "pdf-title"
        ],
        "id": "t4-ErBulx78v"
      },
      "source": [
        "# Softmax exercise\n",
        "\n",
        "*Complete and hand in this completed worksheet (including its outputs and any supporting code outside of the worksheet) with your assignment submission. For more details see the [assignments page](http://vision.stanford.edu/teaching/cs231n/assignments.html) on the course website.*\n",
        "\n",
        "This exercise is analogous to the SVM exercise. You will:\n",
        "\n",
        "- implement a fully-vectorized **loss function** for the Softmax classifier\n",
        "- implement the fully-vectorized expression for its **analytic gradient**\n",
        "- **check your implementation** with numerical gradient\n",
        "- use a validation set to **tune the learning rate and regularization** strength\n",
        "- **optimize** the loss function with **SGD**\n",
        "- **visualize** the final learned weights\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "tags": [
          "pdf-ignore"
        ],
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 892
        },
        "id": "BMqReL31x78w",
        "outputId": "ab569592-d04d-4ef0-ca29-69aa7947a956"
      },
      "source": [
        "import random\n",
        "import numpy as np\n",
        "from cs231n.data_utils import load_CIFAR10\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "%matplotlib inline\n",
        "plt.rcParams['figure.figsize'] = (10.0, 8.0) # set default size of plots\n",
        "plt.rcParams['image.interpolation'] = 'nearest'\n",
        "plt.rcParams['image.cmap'] = 'gray'\n",
        "\n",
        "# for auto-reloading extenrnal modules\n",
        "# see http://stackoverflow.com/questions/1907993/autoreload-of-modules-in-ipython\n",
        "%load_ext autoreload\n",
        "%autoreload 2"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "ERROR:root:Internal Python error in the inspect module.\n",
            "Below is the traceback from this internal error.\n",
            "\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/interactiveshell.py\", line 2882, in run_code\n",
            "    exec(code_obj, self.user_global_ns, self.user_ns)\n",
            "  File \"<ipython-input-15-6ddf828c9a6d>\", line 3, in <module>\n",
            "    from cs231n.data_utils import load_CIFAR10\n",
            "  File \"<frozen importlib._bootstrap>\", line 983, in _find_and_load\n",
            "  File \"<frozen importlib._bootstrap>\", line 963, in _find_and_load_unlocked\n",
            "  File \"<frozen importlib._bootstrap>\", line 906, in _find_spec\n",
            "  File \"<frozen importlib._bootstrap_external>\", line 1280, in find_spec\n",
            "  File \"<frozen importlib._bootstrap_external>\", line 1249, in _get_spec\n",
            "  File \"<frozen importlib._bootstrap_external>\", line 1213, in _path_importer_cache\n",
            "OSError: [Errno 107] Transport endpoint is not connected\n",
            "\n",
            "During handling of the above exception, another exception occurred:\n",
            "\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/interactiveshell.py\", line 1823, in showtraceback\n",
            "    stb = value._render_traceback_()\n",
            "AttributeError: 'OSError' object has no attribute '_render_traceback_'\n",
            "\n",
            "During handling of the above exception, another exception occurred:\n",
            "\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/ultratb.py\", line 1132, in get_records\n",
            "    return _fixed_getinnerframes(etb, number_of_lines_of_context, tb_offset)\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/ultratb.py\", line 313, in wrapped\n",
            "    return f(*args, **kwargs)\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/ultratb.py\", line 358, in _fixed_getinnerframes\n",
            "    records = fix_frame_records_filenames(inspect.getinnerframes(etb, context))\n",
            "  File \"/usr/lib/python3.7/inspect.py\", line 1502, in getinnerframes\n",
            "    frameinfo = (tb.tb_frame,) + getframeinfo(tb, context)\n",
            "  File \"/usr/lib/python3.7/inspect.py\", line 1460, in getframeinfo\n",
            "    filename = getsourcefile(frame) or getfile(frame)\n",
            "  File \"/usr/lib/python3.7/inspect.py\", line 696, in getsourcefile\n",
            "    if getattr(getmodule(object, filename), '__loader__', None) is not None:\n",
            "  File \"/usr/lib/python3.7/inspect.py\", line 725, in getmodule\n",
            "    file = getabsfile(object, _filename)\n",
            "  File \"/usr/lib/python3.7/inspect.py\", line 709, in getabsfile\n",
            "    return os.path.normcase(os.path.abspath(_filename))\n",
            "  File \"/usr/lib/python3.7/posixpath.py\", line 383, in abspath\n",
            "    cwd = os.getcwd()\n",
            "OSError: [Errno 107] Transport endpoint is not connected\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "error",
          "ename": "OSError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "tags": [
          "pdf-ignore"
        ],
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 820
        },
        "id": "QHo9Vyxfx78w",
        "outputId": "4b20024e-ad84-4b81-d124-68fa28c41c9b"
      },
      "source": [
        "def get_CIFAR10_data(num_training=49000, num_validation=1000, num_test=1000, num_dev=500):\n",
        "    \"\"\"\n",
        "    Load the CIFAR-10 dataset from disk and perform preprocessing to prepare\n",
        "    it for the linear classifier. These are the same steps as we used for the\n",
        "    SVM, but condensed to a single function.  \n",
        "    \"\"\"\n",
        "    # Load the raw CIFAR-10 data\n",
        "    cifar10_dir = 'cs231n/datasets/cifar-10-batches-py'\n",
        "    \n",
        "    # Cleaning up variables to prevent loading data multiple times (which may cause memory issue)\n",
        "    try:\n",
        "       del X_train, y_train\n",
        "       del X_test, y_test\n",
        "       print('Clear previously loaded data.')\n",
        "    except:\n",
        "       pass\n",
        "\n",
        "    X_train, y_train, X_test, y_test = load_CIFAR10(cifar10_dir)\n",
        "    \n",
        "    # subsample the data\n",
        "    mask = list(range(num_training, num_training + num_validation))\n",
        "    X_val = X_train[mask]\n",
        "    y_val = y_train[mask]\n",
        "    mask = list(range(num_training))\n",
        "    X_train = X_train[mask]\n",
        "    y_train = y_train[mask]\n",
        "    mask = list(range(num_test))\n",
        "    X_test = X_test[mask]\n",
        "    y_test = y_test[mask]\n",
        "    mask = np.random.choice(num_training, num_dev, replace=False)\n",
        "    X_dev = X_train[mask]\n",
        "    y_dev = y_train[mask]\n",
        "    \n",
        "    # Preprocessing: reshape the image data into rows\n",
        "    X_train = np.reshape(X_train, (X_train.shape[0], -1))\n",
        "    X_val = np.reshape(X_val, (X_val.shape[0], -1))\n",
        "    X_test = np.reshape(X_test, (X_test.shape[0], -1))\n",
        "    X_dev = np.reshape(X_dev, (X_dev.shape[0], -1))\n",
        "    \n",
        "    # Normalize the data: subtract the mean image\n",
        "    mean_image = np.mean(X_train, axis = 0)\n",
        "    X_train -= mean_image\n",
        "    X_val -= mean_image\n",
        "    X_test -= mean_image\n",
        "    X_dev -= mean_image\n",
        "    \n",
        "    # add bias dimension and transform into columns\n",
        "    X_train = np.hstack([X_train, np.ones((X_train.shape[0], 1))])\n",
        "    X_val = np.hstack([X_val, np.ones((X_val.shape[0], 1))])\n",
        "    X_test = np.hstack([X_test, np.ones((X_test.shape[0], 1))])\n",
        "    X_dev = np.hstack([X_dev, np.ones((X_dev.shape[0], 1))])\n",
        "    \n",
        "    return X_train, y_train, X_val, y_val, X_test, y_test, X_dev, y_dev\n",
        "\n",
        "\n",
        "# Invoke the above function to get our data.\n",
        "X_train, y_train, X_val, y_val, X_test, y_test, X_dev, y_dev = get_CIFAR10_data()\n",
        "print('Train data shape: ', X_train.shape)\n",
        "print('Train labels shape: ', y_train.shape)\n",
        "print('Validation data shape: ', X_val.shape)\n",
        "print('Validation labels shape: ', y_val.shape)\n",
        "print('Test data shape: ', X_test.shape)\n",
        "print('Test labels shape: ', y_test.shape)\n",
        "print('dev data shape: ', X_dev.shape)\n",
        "print('dev labels shape: ', y_dev.shape)"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "ERROR:root:Internal Python error in the inspect module.\n",
            "Below is the traceback from this internal error.\n",
            "\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/interactiveshell.py\", line 2882, in run_code\n",
            "    exec(code_obj, self.user_global_ns, self.user_ns)\n",
            "  File \"<ipython-input-17-436d78fe1265>\", line 57, in <module>\n",
            "    X_train, y_train, X_val, y_val, X_test, y_test, X_dev, y_dev = get_CIFAR10_data()\n",
            "  File \"<ipython-input-17-436d78fe1265>\", line 18, in get_CIFAR10_data\n",
            "    X_train, y_train, X_test, y_test = load_CIFAR10(cifar10_dir)\n",
            "NameError: name 'load_CIFAR10' is not defined\n",
            "\n",
            "During handling of the above exception, another exception occurred:\n",
            "\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/interactiveshell.py\", line 1823, in showtraceback\n",
            "    stb = value._render_traceback_()\n",
            "AttributeError: 'NameError' object has no attribute '_render_traceback_'\n",
            "\n",
            "During handling of the above exception, another exception occurred:\n",
            "\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/ultratb.py\", line 1132, in get_records\n",
            "    return _fixed_getinnerframes(etb, number_of_lines_of_context, tb_offset)\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/ultratb.py\", line 313, in wrapped\n",
            "    return f(*args, **kwargs)\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/ultratb.py\", line 358, in _fixed_getinnerframes\n",
            "    records = fix_frame_records_filenames(inspect.getinnerframes(etb, context))\n",
            "  File \"/usr/lib/python3.7/inspect.py\", line 1502, in getinnerframes\n",
            "    frameinfo = (tb.tb_frame,) + getframeinfo(tb, context)\n",
            "  File \"/usr/lib/python3.7/inspect.py\", line 1460, in getframeinfo\n",
            "    filename = getsourcefile(frame) or getfile(frame)\n",
            "  File \"/usr/lib/python3.7/inspect.py\", line 696, in getsourcefile\n",
            "    if getattr(getmodule(object, filename), '__loader__', None) is not None:\n",
            "  File \"/usr/lib/python3.7/inspect.py\", line 725, in getmodule\n",
            "    file = getabsfile(object, _filename)\n",
            "  File \"/usr/lib/python3.7/inspect.py\", line 709, in getabsfile\n",
            "    return os.path.normcase(os.path.abspath(_filename))\n",
            "  File \"/usr/lib/python3.7/posixpath.py\", line 383, in abspath\n",
            "    cwd = os.getcwd()\n",
            "OSError: [Errno 107] Transport endpoint is not connected\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "error",
          "ename": "NameError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "D_AFvZJCx78y"
      },
      "source": [
        "## Softmax Classifier\n",
        "\n",
        "Your code for this section will all be written inside `cs231n/classifiers/softmax.py`.\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "K8MhMjsdx78z",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 892
        },
        "outputId": "25c81c66-2546-4a1d-d2bd-3d37a4dc5c11"
      },
      "source": [
        "# First implement the naive softmax loss function with nested loops.\n",
        "# Open the file cs231n/classifiers/softmax.py and implement the\n",
        "# softmax_loss_naive function.\n",
        "\n",
        "from cs231n.classifiers.softmax import softmax_loss_naive\n",
        "import time\n",
        "\n",
        "# Generate a random softmax weight matrix and use it to compute the loss.\n",
        "W = np.random.randn(3073, 10) * 0.0001\n",
        "loss, grad = softmax_loss_naive(W, X_dev, y_dev, 0.0)\n",
        "\n",
        "# As a rough sanity check, our loss should be something close to -log(0.1).\n",
        "print('loss: %f' % loss)\n",
        "print('sanity check: %f' % (-np.log(0.1)))"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "ERROR:root:Internal Python error in the inspect module.\n",
            "Below is the traceback from this internal error.\n",
            "\n"
          ],
          "name": "stderr"
        },
        {
          "output_type": "stream",
          "text": [
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/interactiveshell.py\", line 2882, in run_code\n",
            "    exec(code_obj, self.user_global_ns, self.user_ns)\n",
            "  File \"<ipython-input-18-704f9686a28b>\", line 5, in <module>\n",
            "    from cs231n.classifiers.softmax import softmax_loss_naive\n",
            "  File \"<frozen importlib._bootstrap>\", line 983, in _find_and_load\n",
            "  File \"<frozen importlib._bootstrap>\", line 963, in _find_and_load_unlocked\n",
            "  File \"<frozen importlib._bootstrap>\", line 906, in _find_spec\n",
            "  File \"<frozen importlib._bootstrap_external>\", line 1280, in find_spec\n",
            "  File \"<frozen importlib._bootstrap_external>\", line 1249, in _get_spec\n",
            "  File \"<frozen importlib._bootstrap_external>\", line 1213, in _path_importer_cache\n",
            "OSError: [Errno 107] Transport endpoint is not connected\n",
            "\n",
            "During handling of the above exception, another exception occurred:\n",
            "\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/interactiveshell.py\", line 1823, in showtraceback\n",
            "    stb = value._render_traceback_()\n",
            "AttributeError: 'OSError' object has no attribute '_render_traceback_'\n",
            "\n",
            "During handling of the above exception, another exception occurred:\n",
            "\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/ultratb.py\", line 1132, in get_records\n",
            "    return _fixed_getinnerframes(etb, number_of_lines_of_context, tb_offset)\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/ultratb.py\", line 313, in wrapped\n",
            "    return f(*args, **kwargs)\n",
            "  File \"/usr/local/lib/python3.7/dist-packages/IPython/core/ultratb.py\", line 358, in _fixed_getinnerframes\n",
            "    records = fix_frame_records_filenames(inspect.getinnerframes(etb, context))\n",
            "  File \"/usr/lib/python3.7/inspect.py\", line 1502, in getinnerframes\n",
            "    frameinfo = (tb.tb_frame,) + getframeinfo(tb, context)\n",
            "  File \"/usr/lib/python3.7/inspect.py\", line 1460, in getframeinfo\n",
            "    filename = getsourcefile(frame) or getfile(frame)\n",
            "  File \"/usr/lib/python3.7/inspect.py\", line 696, in getsourcefile\n",
            "    if getattr(getmodule(object, filename), '__loader__', None) is not None:\n",
            "  File \"/usr/lib/python3.7/inspect.py\", line 725, in getmodule\n",
            "    file = getabsfile(object, _filename)\n",
            "  File \"/usr/lib/python3.7/inspect.py\", line 709, in getabsfile\n",
            "    return os.path.normcase(os.path.abspath(_filename))\n",
            "  File \"/usr/lib/python3.7/posixpath.py\", line 383, in abspath\n",
            "    cwd = os.getcwd()\n",
            "OSError: [Errno 107] Transport endpoint is not connected\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "error",
          "ename": "OSError",
          "evalue": "ignored",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "tags": [
          "pdf-inline"
        ],
        "id": "T9wxTnpdx781"
      },
      "source": [
        "**Inline Question 1**\n",
        "\n",
        "Why do we expect our loss to be close to -log(0.1)? Explain briefly.**\n",
        "\n",
        "$\\color{blue}{\\textit Your Answer:}$ *Fill this in* \n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "5I8keXWIx781"
      },
      "source": [
        "# Complete the implementation of softmax_loss_naive and implement a (naive)\n",
        "# version of the gradient that uses nested loops.\n",
        "loss, grad = softmax_loss_naive(W, X_dev, y_dev, 0.0)\n",
        "\n",
        "# As we did for the SVM, use numeric gradient checking as a debugging tool.\n",
        "# The numeric gradient should be close to the analytic gradient.\n",
        "from cs231n.gradient_check import grad_check_sparse\n",
        "f = lambda w: softmax_loss_naive(w, X_dev, y_dev, 0.0)[0]\n",
        "grad_numerical = grad_check_sparse(f, W, grad, 10)\n",
        "\n",
        "# similar to SVM case, do another gradient check with regularization\n",
        "loss, grad = softmax_loss_naive(W, X_dev, y_dev, 5e1)\n",
        "f = lambda w: softmax_loss_naive(w, X_dev, y_dev, 5e1)[0]\n",
        "grad_numerical = grad_check_sparse(f, W, grad, 10)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-Xrdwlg0x781"
      },
      "source": [
        "# Now that we have a naive implementation of the softmax loss function and its gradient,\n",
        "# implement a vectorized version in softmax_loss_vectorized.\n",
        "# The two versions should compute the same results, but the vectorized version should be\n",
        "# much faster.\n",
        "tic = time.time()\n",
        "loss_naive, grad_naive = softmax_loss_naive(W, X_dev, y_dev, 0.000005)\n",
        "toc = time.time()\n",
        "print('naive loss: %e computed in %fs' % (loss_naive, toc - tic))\n",
        "\n",
        "from cs231n.classifiers.softmax import softmax_loss_vectorized\n",
        "tic = time.time()\n",
        "loss_vectorized, grad_vectorized = softmax_loss_vectorized(W, X_dev, y_dev, 0.000005)\n",
        "toc = time.time()\n",
        "print('vectorized loss: %e computed in %fs' % (loss_vectorized, toc - tic))\n",
        "\n",
        "# As we did for the SVM, we use the Frobenius norm to compare the two versions\n",
        "# of the gradient.\n",
        "grad_difference = np.linalg.norm(grad_naive - grad_vectorized, ord='fro')\n",
        "print('Loss difference: %f' % np.abs(loss_naive - loss_vectorized))\n",
        "print('Gradient difference: %f' % grad_difference)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "tuning",
        "tags": [
          "code"
        ]
      },
      "source": [
        "# Use the validation set to tune hyperparameters (regularization strength and\n",
        "# learning rate). You should experiment with different ranges for the learning\n",
        "# rates and regularization strengths; if you are careful you should be able to\n",
        "# get a classification accuracy of over 0.35 on the validation set.\n",
        "\n",
        "from cs231n.classifiers import Softmax\n",
        "results = {}\n",
        "best_val = -1\n",
        "best_softmax = None\n",
        "\n",
        "################################################################################\n",
        "# TODO:                                                                        #\n",
        "# Use the validation set to set the learning rate and regularization strength. #\n",
        "# This should be identical to the validation that you did for the SVM; save    #\n",
        "# the best trained softmax classifer in best_softmax.                          #\n",
        "################################################################################\n",
        "\n",
        "# Provided as a reference. You may or may not want to change these hyperparameters\n",
        "learning_rates = [1e-7, 5e-7]\n",
        "regularization_strengths = [2.5e4, 5e4]\n",
        "\n",
        "# *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****\n",
        "\n",
        "pass\n",
        "\n",
        "# *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****\n",
        "    \n",
        "# Print out results.\n",
        "for lr, reg in sorted(results):\n",
        "    train_accuracy, val_accuracy = results[(lr, reg)]\n",
        "    print('lr %e reg %e train accuracy: %f val accuracy: %f' % (\n",
        "                lr, reg, train_accuracy, val_accuracy))\n",
        "    \n",
        "print('best validation accuracy achieved during cross-validation: %f' % best_val)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "test"
      },
      "source": [
        "# evaluate on test set\n",
        "# Evaluate the best softmax on test set\n",
        "y_test_pred = best_softmax.predict(X_test)\n",
        "test_accuracy = np.mean(y_test == y_test_pred)\n",
        "print('softmax on raw pixels final test set accuracy: %f' % (test_accuracy, ))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "tags": [
          "pdf-inline"
        ],
        "id": "97doruw8x783"
      },
      "source": [
        "**Inline Question 2** - *True or False*\n",
        "\n",
        "Suppose the overall training loss is defined as the sum of the per-datapoint loss over all training examples. It is possible to add a new datapoint to a training set that would leave the SVM loss unchanged, but this is not the case with the Softmax classifier loss.\n",
        "\n",
        "$\\color{blue}{\\textit Your Answer:}$\n",
        "\n",
        "\n",
        "$\\color{blue}{\\textit Your Explanation:}$\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Jip9dzCpx784"
      },
      "source": [
        "# Visualize the learned weights for each class\n",
        "w = best_softmax.W[:-1,:] # strip out the bias\n",
        "w = w.reshape(32, 32, 3, 10)\n",
        "\n",
        "w_min, w_max = np.min(w), np.max(w)\n",
        "\n",
        "classes = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']\n",
        "for i in range(10):\n",
        "    plt.subplot(2, 5, i + 1)\n",
        "    \n",
        "    # Rescale the weights to be between 0 and 255\n",
        "    wimg = 255.0 * (w[:, :, :, i].squeeze() - w_min) / (w_max - w_min)\n",
        "    plt.imshow(wimg.astype('uint8'))\n",
        "    plt.axis('off')\n",
        "    plt.title(classes[i])"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jk18Xkhdx784"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}