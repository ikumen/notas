interface Note {
  id: string,
  user: string,
  title: string,
  category?: string,
  content?: string,
  published: boolean,
  createdate?: string,
  updatedate?: string,
  tags: Array<string>
};

export type { Note };