const Product = require('../models/Product');

class ProductRepository {
  static async find(query, options) {
    return Product.find(query)
      .sort(options.sort)
      .limit(options.limit);
  }

  static async findById(id) {
    return Product.findById(id);
  }
  static async create(data) {
  return Product.create(data);
}


  static async softDelete(id) {
    return Product.findByIdAndUpdate(
      id,
      { deletedAt: new Date() },
      { new: true }
    );
  }
}

module.exports = ProductRepository;
