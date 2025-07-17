import pytest 

from app import add


stage('Checkout') {
            steps {
               checkout scmGit(
