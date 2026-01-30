const ProductService = require("../services/product.service");
const logger = require("../utils/logger");
const emailQueue = require("../jobs/email.job");

class ProductController {
  static async getProducts(req, res, next) {
    try {
      logger.info("Fetching products", { requestId: req.requestId });

      const products = await ProductService.getProducts(req.query);

      // Enqueue email on every fetch (testing only)
      try {
        await emailQueue.add({
          to: 'devanshcsa@gmail.com',
          subject: 'Products fetched (test email)',
        });
      } catch (emailErr) {
        logger.error("Failed to enqueue email job", {
          requestId: req.requestId,
          error: emailErr.message,
        });
      }

      res.json({ success: true, data: products });
    } catch (err) {
      logger.error("Failed to fetch products", {
        requestId: req.requestId,
        error: err.message,
      });
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

  static async createProduct(req, res, next) {
    try {
      const product = await ProductService.createProduct(req.body);
      res.status(201).json({ success: true, data: product });
    } catch (err) {
      next(err);
    }
  }
}

module.exports = ProductController;
