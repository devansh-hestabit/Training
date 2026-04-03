const AppError = require('../utils/appError');

const validate = (schema, property = 'body') => {
  return (req, res, next) => {
    const { error } = schema.validate(req[property], {
      abortEarly: false,
      stripUnknown: true,
    });

    if (error) {
      const message = error.details.map((d) => d.message).join(', ');
      return next(new AppError(message, 400, 'VALIDATION_ERROR'));
    }

    next();
  };
};

module.exports = validate;
