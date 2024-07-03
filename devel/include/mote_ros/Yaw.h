// Generated by gencpp from file mote_ros/Yaw.msg
// DO NOT EDIT!


#ifndef MOTE_ROS_MESSAGE_YAW_H
#define MOTE_ROS_MESSAGE_YAW_H


#include <string>
#include <vector>
#include <memory>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace mote_ros
{
template <class ContainerAllocator>
struct Yaw_
{
  typedef Yaw_<ContainerAllocator> Type;

  Yaw_()
    : yaw_rad(0.0)
    , yaw_rate(0.0)
    , yaw_x_position(0.0)
    , yaw_y_position(0.0)  {
    }
  Yaw_(const ContainerAllocator& _alloc)
    : yaw_rad(0.0)
    , yaw_rate(0.0)
    , yaw_x_position(0.0)
    , yaw_y_position(0.0)  {
  (void)_alloc;
    }



   typedef double _yaw_rad_type;
  _yaw_rad_type yaw_rad;

   typedef double _yaw_rate_type;
  _yaw_rate_type yaw_rate;

   typedef double _yaw_x_position_type;
  _yaw_x_position_type yaw_x_position;

   typedef double _yaw_y_position_type;
  _yaw_y_position_type yaw_y_position;





  typedef boost::shared_ptr< ::mote_ros::Yaw_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::mote_ros::Yaw_<ContainerAllocator> const> ConstPtr;

}; // struct Yaw_

typedef ::mote_ros::Yaw_<std::allocator<void> > Yaw;

typedef boost::shared_ptr< ::mote_ros::Yaw > YawPtr;
typedef boost::shared_ptr< ::mote_ros::Yaw const> YawConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::mote_ros::Yaw_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::mote_ros::Yaw_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::mote_ros::Yaw_<ContainerAllocator1> & lhs, const ::mote_ros::Yaw_<ContainerAllocator2> & rhs)
{
  return lhs.yaw_rad == rhs.yaw_rad &&
    lhs.yaw_rate == rhs.yaw_rate &&
    lhs.yaw_x_position == rhs.yaw_x_position &&
    lhs.yaw_y_position == rhs.yaw_y_position;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::mote_ros::Yaw_<ContainerAllocator1> & lhs, const ::mote_ros::Yaw_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace mote_ros

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsMessage< ::mote_ros::Yaw_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::mote_ros::Yaw_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mote_ros::Yaw_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::mote_ros::Yaw_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mote_ros::Yaw_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::mote_ros::Yaw_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::mote_ros::Yaw_<ContainerAllocator> >
{
  static const char* value()
  {
    return "1b1bf6d09d1901c86cf97837e897882f";
  }

  static const char* value(const ::mote_ros::Yaw_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x1b1bf6d09d1901c8ULL;
  static const uint64_t static_value2 = 0x6cf97837e897882fULL;
};

template<class ContainerAllocator>
struct DataType< ::mote_ros::Yaw_<ContainerAllocator> >
{
  static const char* value()
  {
    return "mote_ros/Yaw";
  }

  static const char* value(const ::mote_ros::Yaw_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::mote_ros::Yaw_<ContainerAllocator> >
{
  static const char* value()
  {
    return "float64 yaw_rad\n"
"float64 yaw_rate\n"
"float64 yaw_x_position\n"
"float64 yaw_y_position\n"
;
  }

  static const char* value(const ::mote_ros::Yaw_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::mote_ros::Yaw_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.yaw_rad);
      stream.next(m.yaw_rate);
      stream.next(m.yaw_x_position);
      stream.next(m.yaw_y_position);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct Yaw_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::mote_ros::Yaw_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::mote_ros::Yaw_<ContainerAllocator>& v)
  {
    s << indent << "yaw_rad: ";
    Printer<double>::stream(s, indent + "  ", v.yaw_rad);
    s << indent << "yaw_rate: ";
    Printer<double>::stream(s, indent + "  ", v.yaw_rate);
    s << indent << "yaw_x_position: ";
    Printer<double>::stream(s, indent + "  ", v.yaw_x_position);
    s << indent << "yaw_y_position: ";
    Printer<double>::stream(s, indent + "  ", v.yaw_y_position);
  }
};

} // namespace message_operations
} // namespace ros

#endif // MOTE_ROS_MESSAGE_YAW_H
