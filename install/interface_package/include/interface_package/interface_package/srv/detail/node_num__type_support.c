// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from interface_package:srv/NodeNum.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "interface_package/srv/detail/node_num__rosidl_typesupport_introspection_c.h"
#include "interface_package/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "interface_package/srv/detail/node_num__functions.h"
#include "interface_package/srv/detail/node_num__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void interface_package__srv__NodeNum_Request__rosidl_typesupport_introspection_c__NodeNum_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  interface_package__srv__NodeNum_Request__init(message_memory);
}

void interface_package__srv__NodeNum_Request__rosidl_typesupport_introspection_c__NodeNum_Request_fini_function(void * message_memory)
{
  interface_package__srv__NodeNum_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember interface_package__srv__NodeNum_Request__rosidl_typesupport_introspection_c__NodeNum_Request_message_member_array[4] = {
  {
    "current_x",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interface_package__srv__NodeNum_Request, current_x),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "current_y",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interface_package__srv__NodeNum_Request, current_y),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "next_x",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interface_package__srv__NodeNum_Request, next_x),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "next_y",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_INT16,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interface_package__srv__NodeNum_Request, next_y),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers interface_package__srv__NodeNum_Request__rosidl_typesupport_introspection_c__NodeNum_Request_message_members = {
  "interface_package__srv",  // message namespace
  "NodeNum_Request",  // message name
  4,  // number of fields
  sizeof(interface_package__srv__NodeNum_Request),
  interface_package__srv__NodeNum_Request__rosidl_typesupport_introspection_c__NodeNum_Request_message_member_array,  // message members
  interface_package__srv__NodeNum_Request__rosidl_typesupport_introspection_c__NodeNum_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  interface_package__srv__NodeNum_Request__rosidl_typesupport_introspection_c__NodeNum_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t interface_package__srv__NodeNum_Request__rosidl_typesupport_introspection_c__NodeNum_Request_message_type_support_handle = {
  0,
  &interface_package__srv__NodeNum_Request__rosidl_typesupport_introspection_c__NodeNum_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interface_package
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interface_package, srv, NodeNum_Request)() {
  if (!interface_package__srv__NodeNum_Request__rosidl_typesupport_introspection_c__NodeNum_Request_message_type_support_handle.typesupport_identifier) {
    interface_package__srv__NodeNum_Request__rosidl_typesupport_introspection_c__NodeNum_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &interface_package__srv__NodeNum_Request__rosidl_typesupport_introspection_c__NodeNum_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "interface_package/srv/detail/node_num__rosidl_typesupport_introspection_c.h"
// already included above
// #include "interface_package/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "interface_package/srv/detail/node_num__functions.h"
// already included above
// #include "interface_package/srv/detail/node_num__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void interface_package__srv__NodeNum_Response__rosidl_typesupport_introspection_c__NodeNum_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  interface_package__srv__NodeNum_Response__init(message_memory);
}

void interface_package__srv__NodeNum_Response__rosidl_typesupport_introspection_c__NodeNum_Response_fini_function(void * message_memory)
{
  interface_package__srv__NodeNum_Response__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember interface_package__srv__NodeNum_Response__rosidl_typesupport_introspection_c__NodeNum_Response_message_member_array[1] = {
  {
    "success",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_BOOLEAN,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(interface_package__srv__NodeNum_Response, success),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers interface_package__srv__NodeNum_Response__rosidl_typesupport_introspection_c__NodeNum_Response_message_members = {
  "interface_package__srv",  // message namespace
  "NodeNum_Response",  // message name
  1,  // number of fields
  sizeof(interface_package__srv__NodeNum_Response),
  interface_package__srv__NodeNum_Response__rosidl_typesupport_introspection_c__NodeNum_Response_message_member_array,  // message members
  interface_package__srv__NodeNum_Response__rosidl_typesupport_introspection_c__NodeNum_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  interface_package__srv__NodeNum_Response__rosidl_typesupport_introspection_c__NodeNum_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t interface_package__srv__NodeNum_Response__rosidl_typesupport_introspection_c__NodeNum_Response_message_type_support_handle = {
  0,
  &interface_package__srv__NodeNum_Response__rosidl_typesupport_introspection_c__NodeNum_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interface_package
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interface_package, srv, NodeNum_Response)() {
  if (!interface_package__srv__NodeNum_Response__rosidl_typesupport_introspection_c__NodeNum_Response_message_type_support_handle.typesupport_identifier) {
    interface_package__srv__NodeNum_Response__rosidl_typesupport_introspection_c__NodeNum_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &interface_package__srv__NodeNum_Response__rosidl_typesupport_introspection_c__NodeNum_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "interface_package/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "interface_package/srv/detail/node_num__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers interface_package__srv__detail__node_num__rosidl_typesupport_introspection_c__NodeNum_service_members = {
  "interface_package__srv",  // service namespace
  "NodeNum",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // interface_package__srv__detail__node_num__rosidl_typesupport_introspection_c__NodeNum_Request_message_type_support_handle,
  NULL  // response message
  // interface_package__srv__detail__node_num__rosidl_typesupport_introspection_c__NodeNum_Response_message_type_support_handle
};

static rosidl_service_type_support_t interface_package__srv__detail__node_num__rosidl_typesupport_introspection_c__NodeNum_service_type_support_handle = {
  0,
  &interface_package__srv__detail__node_num__rosidl_typesupport_introspection_c__NodeNum_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interface_package, srv, NodeNum_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interface_package, srv, NodeNum_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_interface_package
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interface_package, srv, NodeNum)() {
  if (!interface_package__srv__detail__node_num__rosidl_typesupport_introspection_c__NodeNum_service_type_support_handle.typesupport_identifier) {
    interface_package__srv__detail__node_num__rosidl_typesupport_introspection_c__NodeNum_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)interface_package__srv__detail__node_num__rosidl_typesupport_introspection_c__NodeNum_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interface_package, srv, NodeNum_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, interface_package, srv, NodeNum_Response)()->data;
  }

  return &interface_package__srv__detail__node_num__rosidl_typesupport_introspection_c__NodeNum_service_type_support_handle;
}
