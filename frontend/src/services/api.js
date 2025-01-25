import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000'; // Your FastAPI backend URL

const api = axios.create({
  baseURL: API_BASE_URL,
});

export const getProducts = async () => {
  const response = await api.get('/products');
  return response.data;
};

export const getSuppliers = async () => {
  const response = await api.get('/suppliers');
  return response.data;
};

export const queryProduct = async (query) => {
  const response = await api.get(`/query`, {
    params: { text: query },
  });
  return response.data;
};

export default api;
