const Joi = require('joi');

exports.createUserSchema = Joi.object({
  firstName: Joi.string().trim().min(2).required(),
  lastName: Joi.string().trim().min(2).required(),
  email: Joi.string().email().required(),
  password: Joi.string().min(6).required(),
});
