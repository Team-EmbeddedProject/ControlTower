// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from interface_package:msg/RobotLog.idl
// generated code does not contain a copyright notice

#ifndef INTERFACE_PACKAGE__MSG__DETAIL__ROBOT_LOG__STRUCT_HPP_
#define INTERFACE_PACKAGE__MSG__DETAIL__ROBOT_LOG__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'timestamp'
#include "builtin_interfaces/msg/detail/time__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__interface_package__msg__RobotLog __attribute__((deprecated))
#else
# define DEPRECATED__interface_package__msg__RobotLog __declspec(deprecated)
#endif

namespace interface_package
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct RobotLog_
{
  using Type = RobotLog_<ContainerAllocator>;

  explicit RobotLog_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : timestamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_id = 0l;
      this->latitude = 0.0f;
      this->longitude = 0.0f;
      this->status = "";
    }
  }

  explicit RobotLog_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : timestamp(_alloc, _init),
    status(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->robot_id = 0l;
      this->latitude = 0.0f;
      this->longitude = 0.0f;
      this->status = "";
    }
  }

  // field types and members
  using _timestamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _timestamp_type timestamp;
  using _robot_id_type =
    int32_t;
  _robot_id_type robot_id;
  using _latitude_type =
    float;
  _latitude_type latitude;
  using _longitude_type =
    float;
  _longitude_type longitude;
  using _status_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _status_type status;

  // setters for named parameter idiom
  Type & set__timestamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->timestamp = _arg;
    return *this;
  }
  Type & set__robot_id(
    const int32_t & _arg)
  {
    this->robot_id = _arg;
    return *this;
  }
  Type & set__latitude(
    const float & _arg)
  {
    this->latitude = _arg;
    return *this;
  }
  Type & set__longitude(
    const float & _arg)
  {
    this->longitude = _arg;
    return *this;
  }
  Type & set__status(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->status = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    interface_package::msg::RobotLog_<ContainerAllocator> *;
  using ConstRawPtr =
    const interface_package::msg::RobotLog_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<interface_package::msg::RobotLog_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<interface_package::msg::RobotLog_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      interface_package::msg::RobotLog_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<interface_package::msg::RobotLog_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      interface_package::msg::RobotLog_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<interface_package::msg::RobotLog_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<interface_package::msg::RobotLog_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<interface_package::msg::RobotLog_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__interface_package__msg__RobotLog
    std::shared_ptr<interface_package::msg::RobotLog_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__interface_package__msg__RobotLog
    std::shared_ptr<interface_package::msg::RobotLog_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const RobotLog_ & other) const
  {
    if (this->timestamp != other.timestamp) {
      return false;
    }
    if (this->robot_id != other.robot_id) {
      return false;
    }
    if (this->latitude != other.latitude) {
      return false;
    }
    if (this->longitude != other.longitude) {
      return false;
    }
    if (this->status != other.status) {
      return false;
    }
    return true;
  }
  bool operator!=(const RobotLog_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct RobotLog_

// alias to use template instance with default allocator
using RobotLog =
  interface_package::msg::RobotLog_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace interface_package

#endif  // INTERFACE_PACKAGE__MSG__DETAIL__ROBOT_LOG__STRUCT_HPP_
