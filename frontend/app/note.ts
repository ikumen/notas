export interface Note {
  id: String,
  user: String,
  title?: String,
  category?: String,
  content?: String,
  published: Boolean,
  publishedAt?: Date,
  tags: Array<String>
};
