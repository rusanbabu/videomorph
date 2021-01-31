# -*- coding: utf-8 -*-

# File name: converter.py
#
#   VideoMorph - A PyQt5 frontend to ffmpeg.
#   Copyright 2016-2020 VideoMorph Development Team

#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at

#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

"""This module provides Converter Class."""

from PyQt5.QtCore import QProcess

from .vmpath import LIBRARY_PATH


class Converter:
    """_Converter class to provide conversion functionality."""

    def __init__(self, library_path=LIBRARY_PATH):
        """Class initializer."""
        self._library_path = library_path
        self._process = QProcess()

    def setup_converter(self, reader, finisher):
        """Set up the QProcess object."""
        self._process.setProcessChannelMode(QProcess.MergedChannels)
        self._process.readyRead.connect(reader)
        self._process.finished.connect(finisher)

    def start_converter(self, cmd):
        """Start the encoding process."""
        self._process.start(self._library_path, cmd)

    def stop_converter(self):
        """Terminate the encoding process."""
        self._process.terminate()
        if self.converter_is_running:
            self._process.kill()

    def converter_finished_disconnect(self, connected):
        """Disconnect the QProcess.finished method."""
        self._process.finished.disconnect(connected)

    def close_converter(self):
        """Call QProcess.close method."""
        self._process.close()

    def kill_converter(self):
        """Call QProcess.kill method."""
        self._process.kill()

    def converter_state(self):
        """Call QProcess.state method."""
        return self._process.state()

    def converter_exit_status(self):
        """Call QProcess.exit_status method."""
        return self._process.exitStatus()

    def read_converter_output(self):
        """Call QProcess.readAll method."""
        return str(self._process.readAll())

    @property
    def converter_is_running(self):
        """Return QProcess state."""
        return self._process.state() == QProcess.Running
