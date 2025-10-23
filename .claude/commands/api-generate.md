# Generate Models from API Spec

Generate type-safe models from an OpenAPI or AsyncAPI specification.

## What to do:

1. **Generate models for the requested language(s)**:
   - For TypeScript: `python skills/api.generate-models/modelina_generate.py <spec-path> typescript --output-dir=<output-dir>`
   - For Python: `python skills/api.generate-models/modelina_generate.py <spec-path> python --output-dir=<output-dir>`
   - For other languages: use appropriate generator

2. **Show what was generated**:
   - List all generated files
   - Show a sample of one or two key models
   - Explain how to use them in code

3. **Verify the models**:
   - Check that the files were created
   - Confirm the types are correct
   - Mention any limitations of the simple generator

## Arguments:

- Specification path (required)
- Target language(s) (required): typescript, python, java, go, etc.
- Output directory (optional, has sensible defaults)

## Success Criteria:

- ✅ Models are generated successfully
- ✅ Files are in the correct location
- ✅ User understands how to use the generated code
