// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interface_package:srv/NodeNum.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_PACKAGE__SRV__DETAIL__NODE_NUM__STRUCT_HPP_
#define INTERFACE_PACKAGE__SRV__DETAIL__NODE_NUM__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__interface_package__srv__NodeNum_Request __attribute__((deprecated))
#else
# define DEPRECATED__interface_package__srv__NodeNum_Request __declspec(deprecated)
#endif

namespace interface_package
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct NodeNum_Request_
{
  using Type = NodeNum_Request_<ContainerAllocator>;

  explicit NodeNum_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->current_x = 0;
      this->current_y = 0;
      this->next_x = 0;
      this->next_y = 0;
    }
  }

  explicit NodeNum_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->current_x = 0;
      this->current_y = 0;
      this->next_x = 0;
      this->next_y = 0;
    }
  }

  // field types and members
  using _current_x_type =
    int16_t;
  _current_x_type current_x;
  using _current_y_type =
    int16_t;
  _current_y_type current_y;
  using _next_x_type =
    int16_t;
  _next_x_type next_x;
  using _next_y_type =
    int16_t;
  _next_y_type next_y;

  // setters for named parameter idiom
  Type & set__current_x(
    const int16_t & _arg)
  {
    this->current_x = _arg;
    return *this;
  }
  Type & set__current_y(
    const int16_t & _arg)
  {
    this->current_y = _arg;
    return *this;
  }
  Type & set__next_x(
    const int16_t & _arg)
  {
    this->next_x = _arg;
    return *this;
  }
  Type & set__next_y(
    const int16_t & _arg)
  {
    this->next_y = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interface_package::srv::NodeNum_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const interface_package::srv::NodeNum_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interface_package::srv::NodeNum_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interface_package::srv::NodeNum_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interface_package::srv::NodeNum_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interface_package::srv::NodeNum_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interface_package::srv::NodeNum_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interface_package::srv::NodeNum_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interface_package::srv::NodeNum_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interface_package::srv::NodeNum_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interface_package__srv__NodeNum_Request
    std::shared_ptr<interface_package::srv::NodeNum_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interface_package__srv__NodeNum_Request
    std::shared_ptr<interface_package::srv::NodeNum_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const NodeNum_Request_ & other) const
  {
    if (this->current_x != other.current_x) {
      return false;
    }
    if (this->current_y != other.current_y) {
      return false;
    }
    if (this->next_x != other.next_x) {
      return false;
    }
    if (this->next_y != other.next_y) {
      return false;
    }
    return true;
  }
  bool operator!=(const NodeNum_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct NodeNum_Request_

// alias to use template instance with default allocator
using NodeNum_Request =
  interface_package::srv::NodeNum_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interface_package


#ifndef _WIN32
# define DEPRECATED__interface_package__srv__NodeNum_Response __attribute__((deprecated))
#else
# define DEPRECATED__interface_package__srv__NodeNum_Response __declspec(deprecated)
#endif

namespace interface_package
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct NodeNum_Response_
{
  using Type = NodeNum_Response_<ContainerAllocator>;

  explicit NodeNum_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit NodeNum_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interface_package::srv::NodeNum_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const interface_package::srv::NodeNum_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interface_package::srv::NodeNum_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interface_package::srv::NodeNum_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interface_package::srv::NodeNum_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interface_package::srv::NodeNum_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interface_package::srv::NodeNum_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interface_package::srv::NodeNum_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interface_package::srv::NodeNum_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interface_package::srv::NodeNum_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interface_package__srv__NodeNum_Response
    std::shared_ptr<interface_package::srv::NodeNum_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interface_package__srv__NodeNum_Response
    std::shared_ptr<interface_package::srv::NodeNum_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const NodeNum_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const NodeNum_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct NodeNum_Response_

// alias to use template instance with default allocator
using NodeNum_Response =
  interface_package::srv::NodeNum_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace interface_package

namespace interface_package
{

namespace srv
{

struct NodeNum
{
  using Request = interface_package::srv::NodeNum_Request;
  using Response = interface_package::srv::NodeNum_Response;
};

}  // namespace srv

}  // namespace interface_package

#endif  // INTERFACE_PACKAGE__SRV__DETAIL__NODE_NUM__STRUCT_HPP_
