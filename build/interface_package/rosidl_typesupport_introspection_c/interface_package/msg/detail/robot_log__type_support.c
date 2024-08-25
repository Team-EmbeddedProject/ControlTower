// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from interface_package:msg/RobotLog.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "interface_package/msg/detail/robot_log__rosidl_typesupport_introspection_c.h"
#include "interface_package/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "interface_package/msg/detail/robot_log__functions.h"
#include "interface_package/msg/detail/robot_log__struct.h"


// Include directives for member types
// Member `timestamp`
#include "builtin_interfaces/msg/time.h"
// Member `timestamp`
#include "builtin_interfaces/msg/detail/time__rosidl_typesupport_introspection_c.h"
// Member `status`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__RobotLog_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  interface_package__msg__RobotLog__init(message_memory);
}

void interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__RobotLog_fini_function(void * message_memory)
{
  interface_package__msg__RobotLog__fini(message_memory);
}

size_t interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__size_function__RobotLog__robot_location(
  const void * untyped_member)
{
  (void)untyped_member;
  return 3;
}

const void * interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__get_const_function__RobotLog__robot_location(
  const void * untyped_member, size_t index)
{
  const float * member =
    (const float *)(untyped_member);
  return &member[index];
}

void * interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__get_function__RobotLog__robot_location(
  void * untyped_member, size_t index)
{
  float * member =
    (float *)(untyped_member);
  return &member[index];
}

void interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__fetch_function__RobotLog__robot_location(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const float * item =
    ((const float *)
    interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__get_const_function__RobotLog__robot_location(untyped_member, index));
  float * value =
    (float *)(untyped_value);
  *value = *item;
}

void interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__assign_function__RobotLog__robot_location(
  void * untyped_member, size_t index, const void * untyped_value)
{
  float * item =
    ((float *)
    interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__get_function__RobotLog__robot_location(untyped_member, index));
  const float * value =
    (const float *)(untyped_value);
  *item = *value;
}

static rosidl_typesupport_introspection_c__MessageMember interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__RobotLog_message_member_array[4] = {
  {
    "timestamp",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interface_package__msg__RobotLog, timestamp),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "robot_id",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT32,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interface_package__msg__RobotLog, robot_id),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "robot_location",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    3,  // array size
    false,  // is upper bound
    offsetof(interface_package__msg__RobotLog, robot_location),  // bytes offset in struct
    NULL,  // default value
    interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__size_function__RobotLog__robot_location,  // size() function pointer
    interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__get_const_function__RobotLog__robot_location,  // get_const(index) function pointer
    interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__get_function__RobotLog__robot_location,  // get(index) function pointer
    interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__fetch_function__RobotLog__robot_location,  // fetch(index, &value) function pointer
    interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__assign_function__RobotLog__robot_location,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "status",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interface_package__msg__RobotLog, status),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__RobotLog_message_members = {
  "interface_package__msg",  // message namespace
  "RobotLog",  // message name
  4,  // number of fields
  sizeof(interface_package__msg__RobotLog),
  interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__RobotLog_message_member_array,  // message members
  interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__RobotLog_init_function,  // function to initialize message memory (memory has to be allocated)
  interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__RobotLog_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__RobotLog_message_type_support_handle = {
  0,
  &interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__RobotLog_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interface_package
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interface_package, msg, RobotLog)() {
  interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__RobotLog_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, builtin_interfaces, msg, Time)();
  if (!interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__RobotLog_message_type_support_handle.typesupport_identifier) {
    interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__RobotLog_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &interface_package__msg__RobotLog__rosidl_typesupport_introspection_c__RobotLog_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
