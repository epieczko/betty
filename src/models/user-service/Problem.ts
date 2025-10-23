export interface Problem {
  /** URI reference identifying the problem type */
  type: string;
  /** Short, human-readable summary */
  title: string;
  /** HTTP status code */
  status: number;
  /** Human-readable explanation */
  detail?: string;
  /** URI reference identifying the specific occurrence */
  instance?: string;
}