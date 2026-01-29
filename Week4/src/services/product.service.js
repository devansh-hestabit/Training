const ProductRepository = require('../repositories/product.repository');
const AppError = require('../utils/appError');

class ProductService {
  static async getProducts(queryParams) {
    const {
      search,
      minPrice,
      maxPrice,
      sort,
      limit = 10,
      includeDeleted
    } = queryParams;

    const query = {};

    // 🔹 Soft delete filter
    if (!includeDeleted) {
      query.deletedAt = null;
    }

    // 🔹 Search (regex)
    if (search) {
      query.name = { $regex: search, $options: 'i' };
    }

    // 🔹 Price filtering
    if (minPrice || maxPrice) {
      query.price = {};
      if (minPrice) query.price.$gte = Number(minPrice);
      if (maxPrice) query.price.$lte = Number(maxPrice);
    }

    // 🔹 Sorting
    let sortOption = { createdAt: -1 };
    if (sort) {
      const [field, order] = sort.split(':');
      sortOption = { [field]: order === 'desc' ? -1 : 1 };
    }

    return ProductRepository.find(query, {
      sort: sortOption,
      limit: Number(limit)
    });
  }

  static async deleteProduct(id) {
    const product = await ProductRepository.findById(id);

    if (!product) {
      throw new AppError('Product not found', 404, 'PRODUCT_NOT_FOUND');
    }

    return ProductRepository.softDelete(id);
  }

  static async createProduct(data) {
  return ProductRepository.create(data);
}

}

module.exports = ProductService;
