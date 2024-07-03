// Auto-generated. Do not edit!

// (in-package mote_ros.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Yaw {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.yaw_rad = null;
      this.yaw_rate = null;
      this.yaw_x_position = null;
      this.yaw_y_position = null;
    }
    else {
      if (initObj.hasOwnProperty('yaw_rad')) {
        this.yaw_rad = initObj.yaw_rad
      }
      else {
        this.yaw_rad = 0.0;
      }
      if (initObj.hasOwnProperty('yaw_rate')) {
        this.yaw_rate = initObj.yaw_rate
      }
      else {
        this.yaw_rate = 0.0;
      }
      if (initObj.hasOwnProperty('yaw_x_position')) {
        this.yaw_x_position = initObj.yaw_x_position
      }
      else {
        this.yaw_x_position = 0.0;
      }
      if (initObj.hasOwnProperty('yaw_y_position')) {
        this.yaw_y_position = initObj.yaw_y_position
      }
      else {
        this.yaw_y_position = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Yaw
    // Serialize message field [yaw_rad]
    bufferOffset = _serializer.float64(obj.yaw_rad, buffer, bufferOffset);
    // Serialize message field [yaw_rate]
    bufferOffset = _serializer.float64(obj.yaw_rate, buffer, bufferOffset);
    // Serialize message field [yaw_x_position]
    bufferOffset = _serializer.float64(obj.yaw_x_position, buffer, bufferOffset);
    // Serialize message field [yaw_y_position]
    bufferOffset = _serializer.float64(obj.yaw_y_position, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Yaw
    let len;
    let data = new Yaw(null);
    // Deserialize message field [yaw_rad]
    data.yaw_rad = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [yaw_rate]
    data.yaw_rate = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [yaw_x_position]
    data.yaw_x_position = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [yaw_y_position]
    data.yaw_y_position = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'mote_ros/Yaw';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '1b1bf6d09d1901c86cf97837e897882f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 yaw_rad
    float64 yaw_rate
    float64 yaw_x_position
    float64 yaw_y_position
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Yaw(null);
    if (msg.yaw_rad !== undefined) {
      resolved.yaw_rad = msg.yaw_rad;
    }
    else {
      resolved.yaw_rad = 0.0
    }

    if (msg.yaw_rate !== undefined) {
      resolved.yaw_rate = msg.yaw_rate;
    }
    else {
      resolved.yaw_rate = 0.0
    }

    if (msg.yaw_x_position !== undefined) {
      resolved.yaw_x_position = msg.yaw_x_position;
    }
    else {
      resolved.yaw_x_position = 0.0
    }

    if (msg.yaw_y_position !== undefined) {
      resolved.yaw_y_position = msg.yaw_y_position;
    }
    else {
      resolved.yaw_y_position = 0.0
    }

    return resolved;
    }
};

module.exports = Yaw;
