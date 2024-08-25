// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interface_package:srv/TrashInfo.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_PACKAGE__SRV__DETAIL__TRASH_INFO__STRUCT_H_
#define INTERFACE_PACKAGE__SRV__DETAIL__TRASH_INFO__STRUCT_H_

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
// Member 'trash_type'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/TrashInfo in the package interface_package.
typedef struct interface_package__srv__TrashInfo_Request
{
  builtin_interfaces__msg__Time timestamp;
  int32_t robot_id;
  rosidl_runtime_c__String trash_type;
  float latitude;
  float longitude;
} interface_package__srv__TrashInfo_Request;

// Struct for a sequence of interface_package__srv__TrashInfo_Request.
typedef struct interface_package__srv__TrashInfo_Request__Sequence
{
  interface_package__srv__TrashInfo_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interface_package__srv__TrashInfo_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/TrashInfo in the package interface_package.
typedef struct interface_package__srv__TrashInfo_Response
{
  bool success;
} interface_package__srv__TrashInfo_Response;

// Struct for a sequence of interface_package__srv__TrashInfo_Response.
typedef struct interface_package__srv__TrashInfo_Response__Sequence
{
  interface_package__srv__TrashInfo_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interface_package__srv__TrashInfo_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACE_PACKAGE__SRV__DETAIL__TRASH_INFO__STRUCT_H_
