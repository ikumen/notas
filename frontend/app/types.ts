interface Note {
  id: string,
  user: string,
  title: string,
  category?: string,
  content?: string,
  published: boolean,
  tags: Array<string>
};

export type { Note };