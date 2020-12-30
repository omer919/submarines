"""
Name: Omer Feldman

Class Name: text_protocol_parser.py

Purpose:  Submarines solution

Date: 29/12/2020

Changelog:   29/12/2020 - Init Project
"""

from typing import Tuple, List, Dict
from text_protocol_properties import TextProtocolProperties

ARGUMENTS_INDEX = 1
FIRST_ITEM_INDEX = 0


FIELD_SEPARATOR = "\n"
KEY_VALUE_SEPARATOR = ": "


def check_field(field: str) -> bool:
    return field == TextProtocolProperties.PacketFields.TYPE_FIELD or\
           field == TextProtocolProperties.PacketFields.VERSION_FIELD or\
           field == TextProtocolProperties.PacketFields.STATUS_FIELD or\
           field == TextProtocolProperties.PacketFields.X_COORDINATE or\
           field == TextProtocolProperties.PacketFields.Y_COORDINATE


def check_status(status: str) -> bool:
    return status == TextProtocolProperties.Statuses.AnswerStatus.VICTORY_ATTEMPT or \
           status == TextProtocolProperties.Statuses.AnswerStatus.FULL_SUB_HIT_ATTEMPT or \
           status == TextProtocolProperties.Statuses.AnswerStatus.CORRECT_ATTEMPT or \
           status == TextProtocolProperties.Statuses.AnswerStatus.INCORRECT_ATTEMPT


def check_type(type_argument: str) -> bool:
    return type_argument == TextProtocolProperties.Types.READY or\
           type_argument == TextProtocolProperties.Types.ANSWER or\
           type_argument == TextProtocolProperties.Types.ATTEMPT or\
           type_argument == TextProtocolProperties.Types.ERROR


def check_error_status(error_status: str) -> bool:
    return error_status == TextProtocolProperties.Statuses.ErrorStatues.COORDINATE_OUT_OF_RANGE or\
           error_status == TextProtocolProperties.Statuses.ErrorStatues.CLOSED or\
           error_status == TextProtocolProperties.Statuses.ErrorStatues.ATTEMPT_NOT_IN_TURN or\
           error_status == TextProtocolProperties.Statuses.ErrorStatues.INVALID_PACKET


def check_cord(cord: str) -> bool:
    return cord.isdigit()


def check_parsed_fields(parsed_fields) -> bool:
    """
    version_field = TextProtocolProperties.PacketFields.VERSION_FIELD
    type_field = TextProtocolProperties.PacketFields.TYPE_FIELD
    status_field = TextProtocolProperties.PacketFields.STATUS_FIELD
    x_cord_field = TextProtocolProperties.PacketFields.X_COORDINATE
    y_cord_field = TextProtocolProperties.PacketFields.Y_COORDINATE
    ready_type = TextProtocolProperties.Types.READY
    answer_type = TextProtocolProperties.Types.ANSWER
    attempt_type = TextProtocolProperties.Types.ATTEMPT
    error_type = TextProtocolProperties.Types.ERROR


    if version_field not in parsed_fields:
        return False
    if type_field in parsed_fields and parsed_fields[type_field] == answer_type and (not check_status(parsed_fields[type_field])) or x_cord_field not):
        return False


    """
    pass


def parse_message(message: str):
    """
        parsed_fields = {}
    try:
        lines = message.split('\n')
        print(lines)
        for line in lines:
            print(line)
            field, arguments_string = line.split(": ")
            print(field)
            print(arguments_string)
            if not check_field(field):
                return False, parsed_fields
            arguments = arguments_string[ARGUMENTS_INDEX].split(',')
            print(arguments)
            if (field == TextProtocolProperties.PacketFields.X_COORDINATE or field == TextProtocolProperties.PacketFields.Y_COORDINATE) and not check_cord(arguments):
                return False, parsed_fields
            if len(arguments) > 1:
                parsed_fields[field] = arguments
            else:
                parsed_fields[field] = arguments[FIRST_ITEM_INDEX]
        return True, parsed_fields
    except Exception as error:
        print(error)
        return False, parsed_fields
    """
    try:
        fields = message.split(FIELD_SEPARATOR)
        parsed_fields = {}
        for field in fields[:-1]:

            key, value = field.split(KEY_VALUE_SEPARATOR)
            parsed_fields[key] = value

    except ValueError as error:
        return False, parsed_fields
    return True, parsed_fields
