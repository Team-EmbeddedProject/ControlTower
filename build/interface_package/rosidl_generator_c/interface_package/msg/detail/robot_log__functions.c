// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from interface_package:msg/RobotLog.idl
// generated code does not contain a copyright notice
#include "interface_package/msg/detail/robot_log__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `timestamp`
#include "builtin_interfaces/msg/detail/time__functions.h"
// Member `status`
#include "rosidl_runtime_c/string_functions.h"

bool
interface_package__msg__RobotLog__init(interface_package__msg__RobotLog * msg)
{
  if (!msg) {
    return false;
  }
  // timestamp
  if (!builtin_interfaces__msg__Time__init(&msg->timestamp)) {
    interface_package__msg__RobotLog__fini(msg);
    return false;
  }
  // robot_id
  // latitude
  // longitude
  // status
  if (!rosidl_runtime_c__String__init(&msg->status)) {
    interface_package__msg__RobotLog__fini(msg);
    return false;
  }
  return true;
}

void
interface_package__msg__RobotLog__fini(interface_package__msg__RobotLog * msg)
{
  if (!msg) {
    return;
  }
  // timestamp
  builtin_interfaces__msg__Time__fini(&msg->timestamp);
  // robot_id
  // latitude
  // longitude
  // status
  rosidl_runtime_c__String__fini(&msg->status);
}

bool
interface_package__msg__RobotLog__are_equal(const interface_package__msg__RobotLog * lhs, const interface_package__msg__RobotLog * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // timestamp
  if (!builtin_interfaces__msg__Time__are_equal(
      &(lhs->timestamp), &(rhs->timestamp)))
  {
    return false;
  }
  // robot_id
  if (lhs->robot_id != rhs->robot_id) {
    return false;
  }
  // latitude
  if (lhs->latitude != rhs->latitude) {
    return false;
  }
  // longitude
  if (lhs->longitude != rhs->longitude) {
    return false;
  }
  // status
  if (!rosidl_runtime_c__String__are_equal(
      &(lhs->status), &(rhs->status)))
  {
    return false;
  }
  return true;
}

bool
interface_package__msg__RobotLog__copy(
  const interface_package__msg__RobotLog * input,
  interface_package__msg__RobotLog * output)
{
  if (!input || !output) {
    return false;
  }
  // timestamp
  if (!builtin_interfaces__msg__Time__copy(
      &(input->timestamp), &(output->timestamp)))
  {
    return false;
  }
  // robot_id
  output->robot_id = input->robot_id;
  // latitude
  output->latitude = input->latitude;
  // longitude
  output->longitude = input->longitude;
  // status
  if (!rosidl_runtime_c__String__copy(
      &(input->status), &(output->status)))
  {
    return false;
  }
  return true;
}

interface_package__msg__RobotLog *
interface_package__msg__RobotLog__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interface_package__msg__RobotLog * msg = (interface_package__msg__RobotLog *)allocator.allocate(sizeof(interface_package__msg__RobotLog), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interface_package__msg__RobotLog));
  bool success = interface_package__msg__RobotLog__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
interface_package__msg__RobotLog__destroy(interface_package__msg__RobotLog * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    interface_package__msg__RobotLog__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
interface_package__msg__RobotLog__Sequence__init(interface_package__msg__RobotLog__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interface_package__msg__RobotLog * data = NULL;

  if (size) {
    data = (interface_package__msg__RobotLog *)allocator.zero_allocate(size, sizeof(interface_package__msg__RobotLog), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interface_package__msg__RobotLog__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interface_package__msg__RobotLog__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
interface_package__msg__RobotLog__Sequence__fini(interface_package__msg__RobotLog__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      interface_package__msg__RobotLog__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

interface_package__msg__RobotLog__Sequence *
interface_package__msg__RobotLog__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interface_package__msg__RobotLog__Sequence * array = (interface_package__msg__RobotLog__Sequence *)allocator.allocate(sizeof(interface_package__msg__RobotLog__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = interface_package__msg__RobotLog__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
interface_package__msg__RobotLog__Sequence__destroy(interface_package__msg__RobotLog__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    interface_package__msg__RobotLog__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
interface_package__msg__RobotLog__Sequence__are_equal(const interface_package__msg__RobotLog__Sequence * lhs, const interface_package__msg__RobotLog__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!interface_package__msg__RobotLog__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
interface_package__msg__RobotLog__Sequence__copy(
  const interface_package__msg__RobotLog__Sequence * input,
  interface_package__msg__RobotLog__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(interface_package__msg__RobotLog);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    interface_package__msg__RobotLog * data =
      (interface_package__msg__RobotLog *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!interface_package__msg__RobotLog__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          interface_package__msg__RobotLog__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!interface_package__msg__RobotLog__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
