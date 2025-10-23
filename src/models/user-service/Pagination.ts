export interface Pagination {
  /** Number of items per page */
  limit: number;
  /** Number of items skipped */
  offset: number;
  /** Total number of items available */
  total: number;
}