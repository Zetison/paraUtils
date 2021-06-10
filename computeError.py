from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'XML Structured Grid Reader'
filename1 = '/home/zetison/results/simra/Sula/ideal/M0/hist-1.vts'
filename2 = '/home/zetison/results/simra/Sula/ideal/init.vts'
filename1 = '/home/zetison/results/simra/HuntHill_test_hx100_M0_DNS_uniRef/M0/hist-1.vts'
filename2 = '/home/zetison/results/simra/HuntHill_test_hx100_M0_DNS_uniRef/init.vts'
filename1 = '/home/zetison/results/simra/HuntHill_test_hx100_M0_DNS_uniRef/M0/boun-1.vts'
filename2 = '/home/zetison/results/simra/HuntHill_test_hx100_M0_DNS_uniRef/boun-1.vts'
input1 = XMLStructuredGridReader(registrationName=filename1, FileName=[filename1])
input2 = XMLStructuredGridReader(registrationName=filename2, FileName=[filename2])

# create a new 'Append Attributes'
calculators = [AppendAttributes(registrationName='AppendAttributes1', Input=[input1, input2])]
counter = 0 
for arr in input1.CellArrayStatus:
    counter += 1
    calculators.append(Calculator(registrationName='Calculator_'+arr, Input=calculators[counter-1]))
    calculators[counter].ResultArrayName = 'error_'+arr
    calculators[counter].AttributeType = 'Cell Data'
    calculators[counter].Function = 'abs('+arr+'-'+arr+'_input_1)'

for arr in input1.PointArrayStatus:
    counter += 1
    calculators.append(Calculator(registrationName='Calculator_'+arr, Input=calculators[counter-1]))
    calculators[counter].ResultArrayName = 'error_'+arr
    try:
        calculators[counter].Function = 'abs('+arr+'-'+arr+'_input_1)'
    except:#Assume vector input
        calculators[counter].Function = 'abs('+arr+'_X-'+arr+'_input_1_X)*iHat + '\
                                       +'abs('+arr+'_Y-'+arr+'_input_1_Y)*jHat + '\
                                       +'abs('+arr+'_Z-'+arr+'_input_1_Z)*kHat'

CreateLayout('Layout #2')
integrateVariables1 = IntegrateVariables(registrationName='IntegrateVariables1', Input=calculators[counter])
spreadSheetView1 = CreateView('SpreadSheetView')
integrateVariables1Display = Show(integrateVariables1, spreadSheetView1, 'SpreadSheetRepresentation')
layout2 = GetLayoutByName("Layout #2")
AssignViewToLayout(view=spreadSheetView1, layout=layout2, hint=0)
