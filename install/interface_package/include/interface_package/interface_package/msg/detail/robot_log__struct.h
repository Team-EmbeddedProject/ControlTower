// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interface_package:msg/RobotLog.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_PACKAGE__MSG__DETAIL__ROBOT_LOG__STRUCT_H_
#define INTERFACE_PACKAGE__MSG__DETAIL__ROBOT_LOG__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'timestamp'
#include "builtin_interfaces/msg/detail/time__struct.h"
// Member 'status'
#include "rosidl_runtime_c/string.h"

/// Struct defined in msg/RobotLog in the package interface_package.
typedef struct interface_package__msg__RobotLog
{
  builtin_interfaces__msg__Time timestamp;
  int32_t robot_id;
  float robot_location[3];
  rosidl_runtime_c__String status;
} interface_package__msg__RobotLog;

// Struct for a sequence of interface_package__msg__RobotLog.
typedef struct interface_package__msg__RobotLog__Sequence
{
  interface_package__msg__RobotLog * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interface_package__msg__RobotLog__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACE_PACKAGE__MSG__DETAIL__ROBOT_LOG__STRUCT_H_
