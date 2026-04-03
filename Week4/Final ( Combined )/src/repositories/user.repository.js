const User = require("../models/User");
class UserRepository {
  static async create(data) {
    return User.create(data);
  }
  static async findById(id) {
    return User.findById(id);
  }
  static async findPaginated({ limit = 10, cursor }) {
    const query = cursor ? { _id: { $lt: cursor } } : {};
    return User.find(query).sort({ _id: -1 }).limit(limit);
  }
  static async update(id, data) {
    return User.findByIdAndUpdate(id, data, { new: true });
  }
  static async delete(id) {
    return User.findByIdAndDelete(id);
  }
}
module.exports = UserRepository;
