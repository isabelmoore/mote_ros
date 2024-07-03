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

class Pos {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.act_x_pos = null;
      this.act_y_pos = null;
      this.true_x_pos = null;
      this.true_y_pos = null;
      this.traj_x_pos = null;
      this.traj_y_pos = null;
    }
    else {
      if (initObj.hasOwnProperty('act_x_pos')) {
        this.act_x_pos = initObj.act_x_pos
      }
      else {
        this.act_x_pos = [];
      }
      if (initObj.hasOwnProperty('act_y_pos')) {
        this.act_y_pos = initObj.act_y_pos
      }
      else {
        this.act_y_pos = [];
      }
      if (initObj.hasOwnProperty('true_x_pos')) {
        this.true_x_pos = initObj.true_x_pos
      }
      else {
        this.true_x_pos = [];
      }
      if (initObj.hasOwnProperty('true_y_pos')) {
        this.true_y_pos = initObj.true_y_pos
      }
      else {
        this.true_y_pos = [];
      }
      if (initObj.hasOwnProperty('traj_x_pos')) {
        this.traj_x_pos = initObj.traj_x_pos
      }
      else {
        this.traj_x_pos = [];
      }
      if (initObj.hasOwnProperty('traj_y_pos')) {
        this.traj_y_pos = initObj.traj_y_pos
      }
      else {
        this.traj_y_pos = [];
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Pos
    // Serialize message field [act_x_pos]
    bufferOffset = _arraySerializer.float64(obj.act_x_pos, buffer, bufferOffset, null);
    // Serialize message field [act_y_pos]
    bufferOffset = _arraySerializer.float64(obj.act_y_pos, buffer, bufferOffset, null);
    // Serialize message field [true_x_pos]
    bufferOffset = _arraySerializer.float64(obj.true_x_pos, buffer, bufferOffset, null);
    // Serialize message field [true_y_pos]
    bufferOffset = _arraySerializer.float64(obj.true_y_pos, buffer, bufferOffset, null);
    // Serialize message field [traj_x_pos]
    bufferOffset = _arraySerializer.float64(obj.traj_x_pos, buffer, bufferOffset, null);
    // Serialize message field [traj_y_pos]
    bufferOffset = _arraySerializer.float64(obj.traj_y_pos, buffer, bufferOffset, null);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Pos
    let len;
    let data = new Pos(null);
    // Deserialize message field [act_x_pos]
    data.act_x_pos = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [act_y_pos]
    data.act_y_pos = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [true_x_pos]
    data.true_x_pos = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [true_y_pos]
    data.true_y_pos = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [traj_x_pos]
    data.traj_x_pos = _arrayDeserializer.float64(buffer, bufferOffset, null)
    // Deserialize message field [traj_y_pos]
    data.traj_y_pos = _arrayDeserializer.float64(buffer, bufferOffset, null)
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += 8 * object.act_x_pos.length;
    length += 8 * object.act_y_pos.length;
    length += 8 * object.true_x_pos.length;
    length += 8 * object.true_y_pos.length;
    length += 8 * object.traj_x_pos.length;
    length += 8 * object.traj_y_pos.length;
    return length + 24;
  }

  static datatype() {
    // Returns string type for a message object
    return 'mote_ros/Pos';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '7d1a051bd496b12b36f5467e6e2f8b10';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64[] act_x_pos
    float64[] act_y_pos
    float64[] true_x_pos
    float64[] true_y_pos
    float64[] traj_x_pos
    float64[] traj_y_pos
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Pos(null);
    if (msg.act_x_pos !== undefined) {
      resolved.act_x_pos = msg.act_x_pos;
    }
    else {
      resolved.act_x_pos = []
    }

    if (msg.act_y_pos !== undefined) {
      resolved.act_y_pos = msg.act_y_pos;
    }
    else {
      resolved.act_y_pos = []
    }

    if (msg.true_x_pos !== undefined) {
      resolved.true_x_pos = msg.true_x_pos;
    }
    else {
      resolved.true_x_pos = []
    }

    if (msg.true_y_pos !== undefined) {
      resolved.true_y_pos = msg.true_y_pos;
    }
    else {
      resolved.true_y_pos = []
    }

    if (msg.traj_x_pos !== undefined) {
      resolved.traj_x_pos = msg.traj_x_pos;
    }
    else {
      resolved.traj_x_pos = []
    }

    if (msg.traj_y_pos !== undefined) {
      resolved.traj_y_pos = msg.traj_y_pos;
    }
    else {
      resolved.traj_y_pos = []
    }

    return resolved;
    }
};

module.exports = Pos;
