const Joi = require('joi');

exports.createProductSchema = Joi.object({
  name: Joi.string().trim().min(3).required(),
  price: Joi.number().min(0).required(),
  rating: Joi.number().min(0).max(5),
  status: Joi.string().valid('active', 'inactive'),
});
