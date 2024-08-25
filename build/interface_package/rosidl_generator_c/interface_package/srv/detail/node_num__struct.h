// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from interface_package:srv/NodeNum.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_PACKAGE__SRV__DETAIL__NODE_NUM__STRUCT_H_
#define INTERFACE_PACKAGE__SRV__DETAIL__NODE_NUM__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/NodeNum in the package interface_package.
typedef struct interface_package__srv__NodeNum_Request
{
  int16_t current_x;
  int16_t current_y;
  int16_t next_x;
  int16_t next_y;
} interface_package__srv__NodeNum_Request;

// Struct for a sequence of interface_package__srv__NodeNum_Request.
typedef struct interface_package__srv__NodeNum_Request__Sequence
{
  interface_package__srv__NodeNum_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interface_package__srv__NodeNum_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/NodeNum in the package interface_package.
typedef struct interface_package__srv__NodeNum_Response
{
  bool success;
} interface_package__srv__NodeNum_Response;

// Struct for a sequence of interface_package__srv__NodeNum_Response.
typedef struct interface_package__srv__NodeNum_Response__Sequence
{
  interface_package__srv__NodeNum_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} interface_package__srv__NodeNum_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // INTERFACE_PACKAGE__SRV__DETAIL__NODE_NUM__STRUCT_H_
