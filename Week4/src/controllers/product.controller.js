const ProductService = require('../services/product.service');

class ProductController {
  static async getProducts(req, res, next) {
    try {
      const products = await ProductService.getProducts(req.query);
      res.json({ success: true, data: products });
    } catch (err) {
      next(err);
    }
  }

  static async deleteProduct(req, res, next) {
    try {
      const product = await ProductService.deleteProduct(req.params.id);
      res.json({ success: true, data: product });
    } catch (err) {
      next(err);
    }
  }
}

module.exports = ProductController;
