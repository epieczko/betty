export interface User {
  /** Unique identifier */
  user_id: string;
  /** Creation timestamp */
  created_at: string;
  /** Last update timestamp */
  updated_at?: string;
}