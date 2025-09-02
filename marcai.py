import cv2

def stream_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("No se puede acceder a la cámara.")
        return

    print("Presiona 'q' para salir.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("No se pudo recibir el frame.")
            break

        cv2.imshow('Streaming de Cámara', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    print("Iniciando Marcoai - Streaming básico de cámara")
    stream_camera()

if __name__ == "__main__":
    main()