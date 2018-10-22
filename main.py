def main:
	glutInit(&argc, argv)
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA)

	glutInitWindowSize(800, 600)
	glutCreateWindow("OpenGL lesson 6")

	glutReshapeFunc(reshape)
	glutDisplayFunc(display)
	glutKeyboardFunc(processNormalKeys)
	glutSpecialFunc(processSpecialKeys)
	glutMainLoop()

