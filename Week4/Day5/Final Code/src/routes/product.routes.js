const express = require('express');
const ProductController = require('../controllers/product.controller');
const validate = require('../middlewares/validate');
const { createProductSchema } = require('../validators/product.validator');

const router = express.Router();

// Example (for future POST API)
router.post(
  '/products',
  validate(createProductSchema),
  ProductController.createProduct
);

router.get('/products', ProductController.getProducts);
router.delete('/products/:id', ProductController.deleteProduct);

module.exports = router;
