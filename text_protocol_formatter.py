"""
Name: Omer Feldman

Class Name: text_protocol_formatter.py

Purpose:  Submarines solution

Date: 29/12/2020

Changelog:   29/12/2020 - Init Project
"""

from typing import Tuple, List
from text_protocol_properties import TextProtocolProperties

X_INDEX = 0
Y_INDEX = 1
FIRST_STATUS_INDEX = 0
SECOND_STATUS_INDEX = 1


def create_ready_message() -> str:
    return f"{TextProtocolProperties.PacketFields.VERSION_FIELD}: {TextProtocolProperties.PROTOCOL_VERSION}\n" \
           f"{TextProtocolProperties.PacketFields.TYPE_FIELD}: {TextProtocolProperties.Types.READY}\n\n\n"


def create_attempt_message(coordinate: Tuple[int, int]) -> str:
    return f"{TextProtocolProperties.PacketFields.VERSION_FIELD}: {TextProtocolProperties.PROTOCOL_VERSION}\n" \
           f"{TextProtocolProperties.PacketFields.TYPE_FIELD}: {TextProtocolProperties.Types.ATTEMPT}\n" \
           f"{TextProtocolProperties.PacketFields.X_COORDINATE}: {coordinate[X_INDEX]}\n" \
           f"{TextProtocolProperties.PacketFields.Y_COORDINATE}: {coordinate[Y_INDEX]}\n\n\n"


def create_answer_message(coordinate: Tuple[int, int], statuses: List[str]) -> str:
    if len(statuses) > 1:
        status_line = f"{TextProtocolProperties.PacketFields.STATUS_FIELD}: {statuses[FIRST_STATUS_INDEX]}, {statuses[SECOND_STATUS_INDEX]}"
    else:
        status_line = f"{TextProtocolProperties.PacketFields.STATUS_FIELD}: {statuses[FIRST_STATUS_INDEX]}"
    return f"{TextProtocolProperties.PacketFields.VERSION_FIELD}: {TextProtocolProperties.PROTOCOL_VERSION}\n" \
           f"{TextProtocolProperties.PacketFields.TYPE_FIELD}: {TextProtocolProperties.Types.ANSWER}\n" \
           f"{status_line}\n" \
           f"{TextProtocolProperties.PacketFields.X_COORDINATE}: {coordinate[X_INDEX]}\n" \
           f"{TextProtocolProperties.PacketFields.Y_COORDINATE}: {coordinate[Y_INDEX]}\n\n\n"


def create_error_message(error_status: str) -> str:
    return f"{TextProtocolProperties.PacketFields.VERSION_FIELD}: {TextProtocolProperties.PROTOCOL_VERSION}\n" \
           f"{TextProtocolProperties.PacketFields.TYPE_FIELD}: {TextProtocolProperties.Types.ERROR}\n" \
           f"{TextProtocolProperties.PacketFields.STATUS_FIELD}: {error_status}\n\n\n"
