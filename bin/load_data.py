import json
import os
import sys
import time
from typing import List, Optional, Dict

import progressbar
from dateutil.parser import parse

sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "..")))

import data.db_session as db_session
from data.projects import Project
from data.users import User
from data.ugcs import UGC
from data.projects_ugcs import ProjectUGC


def try_int(text) -> int:
    try:
        return int(text)
    except:
        return 0
