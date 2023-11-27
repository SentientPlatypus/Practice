import cv2
import numpy as np


class Paper:
    A4 = 11.59 * 28
    LETTER = 21.59 * 27.94



class AreaCalculator:
    def __init__(self, name, hand_image:np.ndarray, area_of_paper:float) -> None:
        self.hand_image = hand_image
        self.area_of_paper = area_of_paper
        self.name = name

        self.__hsv_threshold_hue = [0.0, 180.0]
        self.__hsv_threshold_saturation = [0.0, 255.0]
        self.__hsv_threshold_value = [137.58992805755395, 255.0]

    def is_contour_inside(inner_contour, outer_contour):
        for point in inner_contour:
            pt = tuple(map(int, point[0]))
            distance = cv2.pointPolygonTest(outer_contour, pt, False)
            if distance < 0:
                return False
        return True
    
    def calculate_paper_area(self) -> float:
        """Returns area of page in PIXELS"""
        hsvimg = cv2.cvtColor(self.hand_image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsvimg, (self.__hsv_threshold_hue[0], self.__hsv_threshold_saturation[0], self.__hsv_threshold_value[0]),  (self.__hsv_threshold_hue[1], self.__hsv_threshold_saturation[1], self.__hsv_threshold_value[1]))
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours_sorted = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
        paper = contours_sorted[0]
        return paper, cv2.contourArea(paper)
    
    def calculate_hand_area(self, paper_contour) -> float:
        """Returns area detected in hand in PIXELS"""
        gray = cv2.cvtColor(self.hand_image, cv2.COLOR_BGR2GRAY)

        # Step 3: Threshold the image to create a binary image
        _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)


        contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contours = [contour for contour in contours if AreaCalculator.is_contour_inside(contour, paper_contour)]
        contours_sorted = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)
        hand = contours_sorted[0]
        return hand, cv2.contourArea(hand)    
    


    def calculate_area(self) -> float:
        """Calculates the Area of the hand given the area of the paper from the image that it is drawn on in cm"""
        """Calculates the Area of the hand given the area of the paper from the image that it is drawn on in cm"""
        paper_contour, paper_area = self.calculate_paper_area()
        hand_contour, hand_area = self.calculate_hand_area(paper_contour)

        # Draw the paper contour on the original image
        cv2.drawContours(self.hand_image, [hand_contour,], 0, (0, 0, 255), 2)
        cv2.drawContours(self.hand_image, [paper_contour], 0, (0, 0, 255), 2)
        # Get the bounding box of the paper contour
        x_paper, y_paper, w_paper, h_paper = cv2.boundingRect(paper_contour)
        x_hand, y_hand, w_hand, h_hand = cv2.boundingRect(hand_contour)

        # Write the area in the top-left corner of the bounding box
        cv2.putText(self.hand_image, f"Paper Area: {paper_area:.2f} pixels -> {self.area_of_paper}cm^2", (x_paper, y_paper), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 0), 2)
        cv2.putText(self.hand_image, f"Hand Area: {hand_area:.2f} pixels -> {hand_area * (self.area_of_paper / paper_area) :.3f}cm^2", (x_hand, y_hand), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 0), 2)

        print(f"Paper Area (pixels): {paper_area:.2f}, hand area (pixels): {hand_area:.2f}")
        print(f"Paper Area (cm3): {self.area_of_paper}, hand area (cm3): {hand_area * (self.area_of_paper / paper_area) :.3f}")
        # Display the image with the detected contours and areas
        cv2.imshow("Detected Paper and Hand", self.hand_image)
        cv2.imwrite(f"res/{self.name}.png", self.hand_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()




if __name__ == "__main__":
    # areacalculator = AreaCalculator("JUN",  cv2.imread("jundarkhand2.JPG"), Paper.LETTER)
    areacalculator = AreaCalculator("GENE",  cv2.imread("genedarkhand.JPG"), Paper.A4)
    areacalculator.calculate_area()