# Description
A Project to use Images in order to recognize whether a Birth is already in Progress, imminent, or the Cow is not yet ready. Focus on detection of lateryl lying.

# Person Responsible
Dominique Müller

# IMPPORTANT NOTES

Some part of the configuration is highly important and influences the results of the analysis a lot! 
this configuration part is quite specific to the analysed situation in the stable. it is based on the position of the cow in the stable
and the lightning and brightness quality of the image.

AdvancedUnimportantColorRange determines, whether it is already known, which areas of the image can be considered
to be unimportant. Knowing that, the Image Analysis will provide better results. If this information is not available, 
the corresponding variable needs to set to False. In any case, the information, that the light bulb
is at the very bright position will be used, because this is a quite generic Information.

If you now which areas of the image are not important, do the following_
     1. Define Lower and upper Bound of Color in HSV Color Space
     2. Create a Color Range Object with the lower and upper Bound from Step 1.
     3. Add the Color Range Object to the list additionalUnimportantColorRanges
     4. Be Patient And  Have Fun!
    

FILTER_BY_ANGLE determines, whether the contours are beeing filtered by angle. 
If the cow is only able to lay straight in the box, set FILTER_BY_ANGLE to True. This will improve the results.
If the cow is lying next to an empty box and therefore able to lying anyhow, set FILTER_BY_ANGLE to False

If you do have any further questions or remarks, please do not hesitate to contact me: dominique_mueller@gmx.ch

# Contributors And Acknowledgment
## the lecturers to provide Guidance during the Bachelor Thesis  
- Prof. Dr. Patrizio Collovà
- Dr. Klaus-Georg Deck

## the Veterinarian for providing knowledge in their field
- Prof. Dr. med. vet. Gaby Hirsbrunner
- Prof. Dr. Samuel Kohler

## the Sponsor of the Bachelor Thesis and his wife for proding knowledge and improving the results of image capturing with empirical work 
- Nelly Müller
- Peter Müller
