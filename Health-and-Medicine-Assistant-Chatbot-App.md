Last login: Thu Aug 24 00:56:38 on console
(base) kanishkkumar@KALKI-MrcdWar ~ % pip3 install -r requirements.txt
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
(base) kanishkkumar@KALKI-MrcdWar ~ % cd /Users/kanishkkumar/Downloads/Course_3rd_part_3_&_4th_Semester_part-1/Assign GradeS Project/ml_s_kill_hack_2.0
[1] 2268
cd: no such file or directory: /Users/kanishkkumar/Downloads/Course_3rd_part_3_
zsh: no such file or directory: _4th_Semester_part-1/Assign
[1]  + exit 1     cd /Users/kanishkkumar/Downloads/Course_3rd_part_3_
(base) kanishkkumar@KALKI-MrcdWar ~ % cd /Users/kanishkkumar/Downloads/DataScientist/ml_s_kill_hack_2.0
(base) kanishkkumar@KALKI-MrcdWar ml_s_kill_hack_2.0 % pip3 install -r requirements.txt
ERROR: Could not open requirements file: [Errno 2] No such file or directory: 'requirements.txt'
(base) kanishkkumar@KALKI-MrcdWar ml_s_kill_hack_2.0 % pip3 install -r requirements.txt
Requirement already satisfied: df_engine==0.8.1 in /opt/anaconda3/lib/python3.8/site-packages (from -r requirements.txt (line 1)) (0.8.1)
Collecting nltk==3.2.5
  Downloading nltk-3.2.5.tar.gz (1.2 MB)
     |████████████████████████████████| 1.2 MB 8.7 MB/s 
Collecting matplotlib==3.2.2
  Downloading matplotlib-3.2.2-cp38-cp38-macosx_10_9_x86_64.whl (12.5 MB)
     |████████████████████████████████| 12.5 MB 8.5 MB/s 
Collecting numpy==1.19.5
  Downloading numpy-1.19.5-cp38-cp38-macosx_10_9_x86_64.whl (15.6 MB)
     |████████████████████████████████| 15.6 MB 3.8 MB/s 
Collecting torch==1.10.0
  Using cached torch-1.10.0-cp38-none-macosx_10_9_x86_64.whl (147.1 MB)
Requirement already satisfied: pydantic>=1.8.2 in /opt/anaconda3/lib/python3.8/site-packages (from df_engine==0.8.1->-r requirements.txt (line 1)) (1.10.7)
Requirement already satisfied: kiwisolver>=1.0.1 in /opt/anaconda3/lib/python3.8/site-packages (from matplotlib==3.2.2->-r requirements.txt (line 3)) (1.3.1)
Requirement already satisfied: pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 in /opt/anaconda3/lib/python3.8/site-packages (from matplotlib==3.2.2->-r requirements.txt (line 3)) (2.4.7)
Requirement already satisfied: cycler>=0.10 in /opt/anaconda3/lib/python3.8/site-packages (from matplotlib==3.2.2->-r requirements.txt (line 3)) (0.10.0)
Requirement already satisfied: python-dateutil>=2.1 in /opt/anaconda3/lib/python3.8/site-packages (from matplotlib==3.2.2->-r requirements.txt (line 3)) (2.8.1)
Requirement already satisfied: six in /opt/anaconda3/lib/python3.8/site-packages (from nltk==3.2.5->-r requirements.txt (line 2)) (1.15.0)
Requirement already satisfied: typing-extensions in /opt/anaconda3/lib/python3.8/site-packages (from torch==1.10.0->-r requirements.txt (line 5)) (4.5.0)
Building wheels for collected packages: nltk
  Building wheel for nltk (setup.py) ... done
  Created wheel for nltk: filename=nltk-3.2.5-py3-none-any.whl size=1392141 sha256=c74a3bcba9f7bdd0cb2ad336659a075f841b78f6e7e8d61794c234752ebb7fed
  Stored in directory: /Users/kanishkkumar/Library/Caches/pip/wheels/8e/f8/1e/2d246c37b7be22a286ccfb2570fe8ad37177e883cb06cecae6
Successfully built nltk
Installing collected packages: numpy, torch, nltk, matplotlib
  Attempting uninstall: numpy
    Found existing installation: numpy 1.22.4
    Uninstalling numpy-1.22.4:
      Successfully uninstalled numpy-1.22.4
  Attempting uninstall: torch
    Found existing installation: torch 1.8.1
    Uninstalling torch-1.8.1:
      Successfully uninstalled torch-1.8.1
  Attempting uninstall: nltk
    Found existing installation: nltk 3.6.7
    Uninstalling nltk-3.6.7:
      Successfully uninstalled nltk-3.6.7
  Attempting uninstall: matplotlib
    Found existing installation: matplotlib 3.3.4
    Uninstalling matplotlib-3.3.4:
      Successfully uninstalled matplotlib-3.3.4
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
torchvision 0.9.0 requires torch==1.8.0, but you have torch 1.10.0 which is incompatible.
thinc 8.0.13 requires pydantic!=1.8,!=1.8.1,<1.9.0,>=1.7.4, but you have pydantic 1.10.7 which is incompatible.
tf-nightly 2.13.0.dev20230302 requires numpy<1.24,>=1.22, but you have numpy 1.19.5 which is incompatible.
tf-nightly 2.13.0.dev20230302 requires protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.20.3, but you have protobuf 3.20.0 which is incompatible.
tensorflow 2.8.0 requires numpy>=1.20, but you have numpy 1.19.5 which is incompatible.
tensorflow 2.8.0 requires tf-estimator-nightly==2.8.0.dev2021122109, but you have tf-estimator-nightly 2.13.0.dev2023030209 which is incompatible.
tensorboard 2.8.0 requires tensorboard-data-server<0.7.0,>=0.6.0, but you have tensorboard-data-server 0.7.0 which is incompatible.
spacy 3.2.1 requires pydantic!=1.8,!=1.8.1,<1.9.0,>=1.7.4, but you have pydantic 1.10.7 which is incompatible.
socceraction 1.4.0 requires numpy<2.0.0,>=1.21.2, but you have numpy 1.19.5 which is incompatible.
pandas 1.5.3 requires numpy>=1.20.3; python_version < "3.10", but you have numpy 1.19.5 which is incompatible.
jax 0.4.4 requires numpy>=1.20, but you have numpy 1.19.5 which is incompatible.
Successfully installed matplotlib-3.2.2 nltk-3.2.5 numpy-1.19.5 torch-1.10.0
(base) kanishkkumar@KALKI-MrcdWar ml_s_kill_hack_2.0 % python run_interactive.py 
Traceback (most recent call last):
  File "run_interactive.py", line 9, in <module>
    from scenario.response import run_interactive_mode
  File "/Users/kanishkkumar/Downloads/DataScientist/ml_s_kill_hack_2.0/scenario/response.py", line 10, in <module>
    import pandas as pd
  File "/opt/anaconda3/lib/python3.8/site-packages/pandas/__init__.py", line 22, in <module>
    from pandas.compat import is_numpy_dev as _is_numpy_dev  # pyright: ignore # noqa:F401
  File "/opt/anaconda3/lib/python3.8/site-packages/pandas/compat/__init__.py", line 18, in <module>
    from pandas.compat.numpy import (
  File "/opt/anaconda3/lib/python3.8/site-packages/pandas/compat/numpy/__init__.py", line 23, in <module>
    raise ImportError(
ImportError: this version of pandas is incompatible with numpy < 1.20.3
your numpy version is 1.19.5.
Please upgrade numpy to >= 1.20.3 to use this pandas version
(base) kanishkkumar@KALKI-MrcdWar ml_s_kill_hack_2.0 % pip3 update numpy
ERROR: unknown command "update"
(base) kanishkkumar@KALKI-MrcdWar ml_s_kill_hack_2.0 % pip install numpy --upgrade
Requirement already satisfied: numpy in /opt/anaconda3/lib/python3.8/site-packages (1.19.5)
Collecting numpy
  Downloading numpy-1.24.4-cp38-cp38-macosx_10_9_x86_64.whl (19.8 MB)
     |████████████████████████████████| 19.8 MB 3.9 MB/s 
Installing collected packages: numpy
  Attempting uninstall: numpy
    Found existing installation: numpy 1.19.5
    Uninstalling numpy-1.19.5:
      Successfully uninstalled numpy-1.19.5
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
ydata-profiling 4.1.2 requires numpy<1.24,>=1.16.0, but you have numpy 1.24.4 which is incompatible.
torchvision 0.9.0 requires torch==1.8.0, but you have torch 1.10.0 which is incompatible.
thinc 8.0.13 requires pydantic!=1.8,!=1.8.1,<1.9.0,>=1.7.4, but you have pydantic 1.10.7 which is incompatible.
tf-nightly 2.13.0.dev20230302 requires numpy<1.24,>=1.22, but you have numpy 1.24.4 which is incompatible.
tf-nightly 2.13.0.dev20230302 requires protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<5.0.0dev,>=3.20.3, but you have protobuf 3.20.0 which is incompatible.
tensorflow 2.8.0 requires tf-estimator-nightly==2.8.0.dev2021122109, but you have tf-estimator-nightly 2.13.0.dev2023030209 which is incompatible.
tensorboard 2.8.0 requires tensorboard-data-server<0.7.0,>=0.6.0, but you have tensorboard-data-server 0.7.0 which is incompatible.
spacy 3.2.1 requires pydantic!=1.8,!=1.8.1,<1.9.0,>=1.7.4, but you have pydantic 1.10.7 which is incompatible.
scipy 1.6.2 requires numpy<1.23.0,>=1.16.5, but you have numpy 1.24.4 which is incompatible.
Successfully installed numpy-1.24.4
(base) kanishkkumar@KALKI-MrcdWar ml_s_kill_hack_2.0 % python run_interactive.py 
Traceback (most recent call last):
  File "run_interactive.py", line 9, in <module>
    from scenario.response import run_interactive_mode
  File "/Users/kanishkkumar/Downloads/DataScientist/ml_s_kill_hack_2.0/scenario/response.py", line 14, in <module>
    data = pd.read_csv("untitled.csv")
  File "/opt/anaconda3/lib/python3.8/site-packages/pandas/util/_decorators.py", line 211, in wrapper
    return func(*args, **kwargs)
  File "/opt/anaconda3/lib/python3.8/site-packages/pandas/util/_decorators.py", line 331, in wrapper
    return func(*args, **kwargs)
  File "/opt/anaconda3/lib/python3.8/site-packages/pandas/io/parsers/readers.py", line 950, in read_csv
    return _read(filepath_or_buffer, kwds)
  File "/opt/anaconda3/lib/python3.8/site-packages/pandas/io/parsers/readers.py", line 605, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
  File "/opt/anaconda3/lib/python3.8/site-packages/pandas/io/parsers/readers.py", line 1442, in __init__
    self._engine = self._make_engine(f, self.engine)
  File "/opt/anaconda3/lib/python3.8/site-packages/pandas/io/parsers/readers.py", line 1735, in _make_engine
    self.handles = get_handle(
  File "/opt/anaconda3/lib/python3.8/site-packages/pandas/io/common.py", line 856, in get_handle
    handle = open(
FileNotFoundError: [Errno 2] No such file or directory: 'untitled.csv'
(base) kanishkkumar@KALKI-MrcdWar ml_s_kill_hack_2.0 % python run_interactive.py 
type your answer: Hi
2023-08-24 01:24:55,721-           root: 32:        turn_handler():INFO - in_request=Hi ->
 Hi I'm Health and medicine Chatbot Assitant, how may help you?
exec time = 0.009s
type your answer: i want a doctor
2023-08-24 01:25:12,015-           root: 32:        turn_handler():INFO - in_request=i want a doctor ->
 There is a many doctor like following:
- Physicians
- Cardiologists
- Gastroenterologists
- Dentist
- ENT specialist
- Gynaecologist
Please write type of doctor according above way
exec time = 0.012s
type your answer: Cardiologists
2023-08-24 01:25:20,714-           root: 32:        turn_handler():INFO - in_request=Cardiologists ->
 OK! I have book a appointment of cardiologists Doctor for you Sir
exec time = 0.015s
type your answer: thank
2023-08-24 01:25:41,253-           root: 32:        turn_handler():INFO - in_request=thank ->
 Sure Sir, I thanks for your visit but your can go other services if needed you can type 'hi'
exec time = 0.014s
type your answer: hi
2023-08-24 01:25:46,682-           root: 32:        turn_handler():INFO - in_request=hi ->
 Hi I'm Health and medicine Chatbot Assitant, how may help you?
exec time = 0.010s
type your answer: doctor
2023-08-24 01:25:53,987-           root: 32:        turn_handler():INFO - in_request=doctor ->
 There is a many doctor like following:
- Physicians
- Cardiologists
- Gastroenterologists
- Dentist
- ENT specialist
- Gynaecologist
Please write type of doctor according above way
exec time = 0.007s
type your answer: ENT specialist
2023-08-24 01:26:02,868-           root: 32:        turn_handler():INFO - in_request=ENT specialist ->
 OK! I have book a appointment of ent specialist Doctor for you Sir
exec time = 0.011s
type your answer: 
