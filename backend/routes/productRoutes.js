import express from 'express';

import {
  getProducts,
  getProductById,
  createProductReview,
  getTopProducts,
} from '../controllers/productController.js';
import { protect } from '../middleware/authMiddleware.js';
const router = express.Router();

router.route('/').get(getProducts);
router.route('/:id').get(getProductById);
router.route('/:id/reviews').post(protect, createProductReview);
router.get('/top', getTopProducts);
export default router;
