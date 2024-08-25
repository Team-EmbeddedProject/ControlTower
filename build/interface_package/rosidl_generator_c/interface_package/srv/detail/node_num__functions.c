// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from interface_package:srv/NodeNum.idl
// generated code does not contain a copyright notice
#include "interface_package/srv/detail/node_num__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
interface_package__srv__NodeNum_Request__init(interface_package__srv__NodeNum_Request * msg)
{
  if (!msg) {
    return false;
  }
  // current_x
  // current_y
  // next_x
  // next_y
  return true;
}

void
interface_package__srv__NodeNum_Request__fini(interface_package__srv__NodeNum_Request * msg)
{
  if (!msg) {
    return;
  }
  // current_x
  // current_y
  // next_x
  // next_y
}

bool
interface_package__srv__NodeNum_Request__are_equal(const interface_package__srv__NodeNum_Request * lhs, const interface_package__srv__NodeNum_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // current_x
  if (lhs->current_x != rhs->current_x) {
    return false;
  }
  // current_y
  if (lhs->current_y != rhs->current_y) {
    return false;
  }
  // next_x
  if (lhs->next_x != rhs->next_x) {
    return false;
  }
  // next_y
  if (lhs->next_y != rhs->next_y) {
    return false;
  }
  return true;
}

bool
interface_package__srv__NodeNum_Request__copy(
  const interface_package__srv__NodeNum_Request * input,
  interface_package__srv__NodeNum_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // current_x
  output->current_x = input->current_x;
  // current_y
  output->current_y = input->current_y;
  // next_x
  output->next_x = input->next_x;
  // next_y
  output->next_y = input->next_y;
  return true;
}

interface_package__srv__NodeNum_Request *
interface_package__srv__NodeNum_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interface_package__srv__NodeNum_Request * msg = (interface_package__srv__NodeNum_Request *)allocator.allocate(sizeof(interface_package__srv__NodeNum_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interface_package__srv__NodeNum_Request));
  bool success = interface_package__srv__NodeNum_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
interface_package__srv__NodeNum_Request__destroy(interface_package__srv__NodeNum_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    interface_package__srv__NodeNum_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
interface_package__srv__NodeNum_Request__Sequence__init(interface_package__srv__NodeNum_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interface_package__srv__NodeNum_Request * data = NULL;

  if (size) {
    data = (interface_package__srv__NodeNum_Request *)allocator.zero_allocate(size, sizeof(interface_package__srv__NodeNum_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interface_package__srv__NodeNum_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interface_package__srv__NodeNum_Request__fini(&data[i - 1]);
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
interface_package__srv__NodeNum_Request__Sequence__fini(interface_package__srv__NodeNum_Request__Sequence * array)
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
      interface_package__srv__NodeNum_Request__fini(&array->data[i]);
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

interface_package__srv__NodeNum_Request__Sequence *
interface_package__srv__NodeNum_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interface_package__srv__NodeNum_Request__Sequence * array = (interface_package__srv__NodeNum_Request__Sequence *)allocator.allocate(sizeof(interface_package__srv__NodeNum_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = interface_package__srv__NodeNum_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
interface_package__srv__NodeNum_Request__Sequence__destroy(interface_package__srv__NodeNum_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    interface_package__srv__NodeNum_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
interface_package__srv__NodeNum_Request__Sequence__are_equal(const interface_package__srv__NodeNum_Request__Sequence * lhs, const interface_package__srv__NodeNum_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!interface_package__srv__NodeNum_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
interface_package__srv__NodeNum_Request__Sequence__copy(
  const interface_package__srv__NodeNum_Request__Sequence * input,
  interface_package__srv__NodeNum_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(interface_package__srv__NodeNum_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    interface_package__srv__NodeNum_Request * data =
      (interface_package__srv__NodeNum_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!interface_package__srv__NodeNum_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          interface_package__srv__NodeNum_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!interface_package__srv__NodeNum_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
interface_package__srv__NodeNum_Response__init(interface_package__srv__NodeNum_Response * msg)
{
  if (!msg) {
    return false;
  }
  // success
  return true;
}

void
interface_package__srv__NodeNum_Response__fini(interface_package__srv__NodeNum_Response * msg)
{
  if (!msg) {
    return;
  }
  // success
}

bool
interface_package__srv__NodeNum_Response__are_equal(const interface_package__srv__NodeNum_Response * lhs, const interface_package__srv__NodeNum_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // success
  if (lhs->success != rhs->success) {
    return false;
  }
  return true;
}

bool
interface_package__srv__NodeNum_Response__copy(
  const interface_package__srv__NodeNum_Response * input,
  interface_package__srv__NodeNum_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // success
  output->success = input->success;
  return true;
}

interface_package__srv__NodeNum_Response *
interface_package__srv__NodeNum_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interface_package__srv__NodeNum_Response * msg = (interface_package__srv__NodeNum_Response *)allocator.allocate(sizeof(interface_package__srv__NodeNum_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(interface_package__srv__NodeNum_Response));
  bool success = interface_package__srv__NodeNum_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
interface_package__srv__NodeNum_Response__destroy(interface_package__srv__NodeNum_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    interface_package__srv__NodeNum_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
interface_package__srv__NodeNum_Response__Sequence__init(interface_package__srv__NodeNum_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interface_package__srv__NodeNum_Response * data = NULL;

  if (size) {
    data = (interface_package__srv__NodeNum_Response *)allocator.zero_allocate(size, sizeof(interface_package__srv__NodeNum_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = interface_package__srv__NodeNum_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        interface_package__srv__NodeNum_Response__fini(&data[i - 1]);
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
interface_package__srv__NodeNum_Response__Sequence__fini(interface_package__srv__NodeNum_Response__Sequence * array)
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
      interface_package__srv__NodeNum_Response__fini(&array->data[i]);
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

interface_package__srv__NodeNum_Response__Sequence *
interface_package__srv__NodeNum_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  interface_package__srv__NodeNum_Response__Sequence * array = (interface_package__srv__NodeNum_Response__Sequence *)allocator.allocate(sizeof(interface_package__srv__NodeNum_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = interface_package__srv__NodeNum_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
interface_package__srv__NodeNum_Response__Sequence__destroy(interface_package__srv__NodeNum_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    interface_package__srv__NodeNum_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
interface_package__srv__NodeNum_Response__Sequence__are_equal(const interface_package__srv__NodeNum_Response__Sequence * lhs, const interface_package__srv__NodeNum_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!interface_package__srv__NodeNum_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
interface_package__srv__NodeNum_Response__Sequence__copy(
  const interface_package__srv__NodeNum_Response__Sequence * input,
  interface_package__srv__NodeNum_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(interface_package__srv__NodeNum_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    interface_package__srv__NodeNum_Response * data =
      (interface_package__srv__NodeNum_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!interface_package__srv__NodeNum_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          interface_package__srv__NodeNum_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!interface_package__srv__NodeNum_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
