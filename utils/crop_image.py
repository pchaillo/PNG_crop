"""
Contributeurs : Paul Chaillou, Thibaud Picinalli, Tinhinane Smail
"""

import cv2
import numpy as np


def crop_image(image_path):
    """
    Coupe un nuage de points en fonction de la projection 2D d'une image.

    Parameters:
    - image_path (str): Chemin de l'image.
    - points_cloud (numpy.ndarray): Nuage de points en 3D.
    - couleurs (numpy.ndarray): Couleurs associées aux points.
    - h (int): Longueur de l'image.
    - tableau_indice (list): Tableau des indices du nuage de points initial.

    Returns:
    - tuple: Tuple contenant le nuage de points, les couleurs, et le tableau d'indices (si fourni).
    """

    # Variables globales pour stocker les coordonnées des clics souris

    start_x, start_y = -1, -1
    end_x, end_y = -1, -1
    cropping = False

    def mouse_click(event, x, y, flags, param):
        # Référence aux variables globales
        nonlocal start_x, start_y, end_x, end_y, cropping

        if event == cv2.EVENT_LBUTTONDOWN:
            # Début du cropping
            start_x, start_y = x, y
            end_x, end_y = x, y
            cropping = True

        elif event == cv2.EVENT_LBUTTONUP:
            # Fin du cropping
            end_x, end_y = x, y
            cropping = False
            # Dessine le rectangle de cropping
            cv2.rectangle(image_copy, (start_x, start_y),
                          (end_x, end_y), (0, 255, 0), 2)
            cv2.imshow("Cropping", image_copy)

    # Charger l'image
    image = cv2.imread(image_path)
    if image is None:
        print("Erreur: Impossible de charger l'image. Veuillez vérifier le chemin.")
        return None

    image_copy = image.copy()

    # Créer une fenêtre pour l'image
    cv2.namedWindow("Cropping")
    cv2.setMouseCallback("Cropping", mouse_click)

    # Instructions pour l'utilisateur
    print("Utilisez la souris pour sélectionner le rectangle de recadrage. Appuyez sur la touche 'c' puis 'q' pour terminer le recadrage.")

            
    # size = [200,300]
    # fx = 0.5
    # fy = 0.5 

    # Boucle principale
    while True:
        # cv2.resize(image_copy, size,fx,fy)
        cv2.imshow("Cropping", image_copy)
        key = cv2.waitKey(1) & 0xFF

        # Quitter la boucle si la touche "c" est pressée
        if key == ord("c"):
            break

    # Vérifier si le rectangle de recadrage a une taille valide
    if start_x == end_x or start_y == end_y:
        print("Erreur: Le rectangle de recadrage a une taille invalide.")
        return None

    # Récupérer les coordonnées de cropping
    x_min, y_min = min(start_x, end_x), min(start_y, end_y)
    x_max, y_max = max(start_x, end_x), max(start_y, end_y)

    return image[x_min:x_max,y_min:y_max]

    # # Filtrage du nuage de points 
    # bottom_left_corner = (y_min-1)*h + x_min
    # top_left_corner = (y_max-1)*h + x_min
    # bottom_right_corner = (y_min-1)*h + x_max


    # Partie du code spécifique aux nuages de points : pas utilisé ici
    # i = 0
    # points_cloud_crop = []
    # couleurs_crop = []
    # tableau_indice_crop = []

    # while (bottom_left_corner != top_left_corner):
    #     for j in range(bottom_left_corner, bottom_right_corner):
    #         points_cloud_crop.append(points_cloud[j])
    #         couleurs_crop.append(couleurs[j])
    #         if len(tableau_indice) > 0:
    #             tableau_indice_crop.append(tableau_indice[j])
    #     bottom_left_corner = (y_min+i-1)*h + x_min
    #     bottom_right_corner = (y_min+i-1)*h + x_max
    #     i += 1

    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    # if len(tableau_indice_crop) > 0:
    #     return np.array(points_cloud_crop), np.array(couleurs_crop), np.array(tableau_indice_crop)
    # else:
    #     return np.array(points_cloud_crop), np.array(couleurs_crop)
