# generated from rosidl_generator_py/resource/_idl.py.em
# with input from interface_package:srv/NodeNum.idl
# generated code does not contain a copyright notice


# Import statements for member types

import builtins  # noqa: E402, I100

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_NodeNum_Request(type):
    """Metaclass of message 'NodeNum_Request'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('interface_package')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'interface_package.srv.NodeNum_Request')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__node_num__request
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__node_num__request
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__node_num__request
            cls._TYPE_SUPPORT = module.type_support_msg__srv__node_num__request
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__node_num__request

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NodeNum_Request(metaclass=Metaclass_NodeNum_Request):
    """Message class 'NodeNum_Request'."""

    __slots__ = [
        '_current_x',
        '_current_y',
        '_next_x',
        '_next_y',
    ]

    _fields_and_field_types = {
        'current_x': 'int16',
        'current_y': 'int16',
        'next_x': 'int16',
        'next_y': 'int16',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
        rosidl_parser.definition.BasicType('int16'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.current_x = kwargs.get('current_x', int())
        self.current_y = kwargs.get('current_y', int())
        self.next_x = kwargs.get('next_x', int())
        self.next_y = kwargs.get('next_y', int())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.current_x != other.current_x:
            return False
        if self.current_y != other.current_y:
            return False
        if self.next_x != other.next_x:
            return False
        if self.next_y != other.next_y:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def current_x(self):
        """Message field 'current_x'."""
        return self._current_x

    @current_x.setter
    def current_x(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'current_x' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'current_x' field must be an integer in [-32768, 32767]"
        self._current_x = value

    @builtins.property
    def current_y(self):
        """Message field 'current_y'."""
        return self._current_y

    @current_y.setter
    def current_y(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'current_y' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'current_y' field must be an integer in [-32768, 32767]"
        self._current_y = value

    @builtins.property
    def next_x(self):
        """Message field 'next_x'."""
        return self._next_x

    @next_x.setter
    def next_x(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'next_x' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'next_x' field must be an integer in [-32768, 32767]"
        self._next_x = value

    @builtins.property
    def next_y(self):
        """Message field 'next_y'."""
        return self._next_y

    @next_y.setter
    def next_y(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'next_y' field must be of type 'int'"
            assert value >= -32768 and value < 32768, \
                "The 'next_y' field must be an integer in [-32768, 32767]"
        self._next_y = value


# Import statements for member types

# already imported above
# import builtins

# already imported above
# import rosidl_parser.definition


class Metaclass_NodeNum_Response(type):
    """Metaclass of message 'NodeNum_Response'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('interface_package')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'interface_package.srv.NodeNum_Response')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__srv__node_num__response
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__srv__node_num__response
            cls._CONVERT_TO_PY = module.convert_to_py_msg__srv__node_num__response
            cls._TYPE_SUPPORT = module.type_support_msg__srv__node_num__response
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__srv__node_num__response

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class NodeNum_Response(metaclass=Metaclass_NodeNum_Response):
    """Message class 'NodeNum_Response'."""

    __slots__ = [
        '_success',
    ]

    _fields_and_field_types = {
        'success': 'boolean',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.success = kwargs.get('success', bool())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.success != other.success:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @builtins.property
    def success(self):
        """Message field 'success'."""
        return self._success

    @success.setter
    def success(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'success' field must be of type 'bool'"
        self._success = value


class Metaclass_NodeNum(type):
    """Metaclass of service 'NodeNum'."""

    _TYPE_SUPPORT = None

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('interface_package')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'interface_package.srv.NodeNum')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._TYPE_SUPPORT = module.type_support_srv__srv__node_num

            from interface_package.srv import _node_num
            if _node_num.Metaclass_NodeNum_Request._TYPE_SUPPORT is None:
                _node_num.Metaclass_NodeNum_Request.__import_type_support__()
            if _node_num.Metaclass_NodeNum_Response._TYPE_SUPPORT is None:
                _node_num.Metaclass_NodeNum_Response.__import_type_support__()


class NodeNum(metaclass=Metaclass_NodeNum):
    from interface_package.srv._node_num import NodeNum_Request as Request
    from interface_package.srv._node_num import NodeNum_Response as Response

    def __init__(self):
        raise NotImplementedError('Service classes can not be instantiated')
