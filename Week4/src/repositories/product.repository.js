const Product = require('../models/Product');

class ProductRepository {
  static create(data) {
    return Product.create(data);
  }

  static findById(id) {
    return Product.findById(id);
  }

  static findPaginated({ limit = 10, cursor }) {
    const query = cursor ? { _id: { $lt: cursor } } : {};
    return Product.find(query).sort({ _id: -1 }).limit(limit);
  }

  static update(id, data) {
    return Product.findByIdAndUpdate(id, data, { new: true });
  }

  static delete(id) {
    return Product.findByIdAndDelete(id);
  }
}

module.exports = ProductRepository;
